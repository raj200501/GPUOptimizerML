import subprocess

class GpuService:
    def get_gpu_stats(self):
        result = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu,memory.total,memory.free,memory.used', '--format=csv,nounits,noheader'], stdout=subprocess.PIPE)
        stats = result.stdout.decode('utf-8').strip().split('\n')
        gpu_stats = [dict(zip(['utilization', 'memory_total', 'memory_free', 'memory_used'], stat.split(', '))) for stat in stats]
        return gpu_stats
