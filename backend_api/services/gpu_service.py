import subprocess
import shutil

class GpuService:
    def get_gpu_stats(self):
        if not shutil.which("nvidia-smi"):
            return [
                {
                    "utilization": "0",
                    "memory_total": "0",
                    "memory_free": "0",
                    "memory_used": "0",
                    "note": "nvidia-smi not available",
                }
            ]
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=utilization.gpu,memory.total,memory.free,memory.used",
                "--format=csv,nounits,noheader",
            ],
            stdout=subprocess.PIPE,
            check=False,
        )
        stats = result.stdout.decode("utf-8").strip().split("\n")
        gpu_stats = [
            dict(
                zip(
                    ["utilization", "memory_total", "memory_free", "memory_used"],
                    stat.split(", "),
                )
            )
            for stat in stats
            if stat
        ]
        return gpu_stats
