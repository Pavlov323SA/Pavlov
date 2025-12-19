import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Время выполнения: {elapsed_time:.2f} сек")
        return False


if __name__ == "__main__":
    with Timer():
        time.sleep(1.5)