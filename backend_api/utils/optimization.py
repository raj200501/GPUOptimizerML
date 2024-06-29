import torch
from torch2trt import torch2trt
import os
import logging

logging.basicConfig(level=logging.INFO)

def optimize_model(filepath):
    """
    Optimizes a PyTorch model by converting it to TensorRT format for faster inference.
    """
    try:
        # Load the PyTorch model
        model = torch.load(filepath)
        model.eval()  # Set the model to evaluation mode

        # Example input for the model (dummy input)
        example_input = torch.randn(1, 3, 224, 224)

        # Convert the PyTorch model to TensorRT
        model_trt = torch2trt(model, [example_input])

        # Save the optimized TensorRT model
        optimized_filepath = os.path.splitext(filepath)[0] + '_optimized_trt.pth'
        torch.save(model_trt, optimized_filepath)

        logging.info(f"Model optimized successfully: {optimized_filepath}")

        return optimized_filepath

    except Exception as e:
        logging.error(f"Error during model optimization: {e}")
        raise e
