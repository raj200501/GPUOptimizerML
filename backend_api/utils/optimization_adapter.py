import importlib
import importlib.util
import logging
import os

logger = logging.getLogger(__name__)


def _dependency_available(module_name):
    return importlib.util.find_spec(module_name) is not None


def _fallback_copy(filepath, reason):
    logger.warning("Optimization fallback used: %s", reason)
    optimized_filepath = os.path.splitext(filepath)[0] + "_optimized_trt.pth"
    with open(filepath, "rb") as source_file:
        with open(optimized_filepath, "wb") as target_file:
            target_file.write(source_file.read())
    return optimized_filepath


def optimize_model_compat(filepath):
    """
    Optimizes a PyTorch model by converting it to TensorRT format when available.
    Falls back to a safe copy when dependencies or GPU tooling are missing.
    """
    if not _dependency_available("torch") or not _dependency_available("torch2trt"):
        return _fallback_copy(filepath, "torch/torch2trt not available")

    torch = importlib.import_module("torch")
    torch2trt_module = importlib.import_module("torch2trt")
    torch2trt = getattr(torch2trt_module, "torch2trt", None)
    if torch2trt is None:
        return _fallback_copy(filepath, "torch2trt missing torch2trt()")

    try:
        model = torch.load(filepath)
        model.eval()
        example_input = torch.randn(1, 3, 224, 224)
        model_trt = torch2trt(model, [example_input])
        optimized_filepath = os.path.splitext(filepath)[0] + "_optimized_trt.pth"
        torch.save(model_trt, optimized_filepath)
        logger.info("Model optimized successfully: %s", optimized_filepath)
        return optimized_filepath
    except Exception as exc:
        return _fallback_copy(filepath, f"optimization error: {exc}")
