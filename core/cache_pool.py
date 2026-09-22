import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)

class CollectiveCachePool:
    def __init__(self, pool_dir="./collective_sandbox_cache"):
        self.pool_dir = pool_dir
        self.setup_pool()

    def setup_pool(self):
        """Khởi tạo bể tài nguyên chung, xóa sạch mọi tàn dư cũ"""
        if os.path.exists(self.pool_dir):
            shutil.rmtree(self.pool_dir)
        os.makedirs(self.pool_dir)
        logging.info(f"🛡️ [CACHE POOL] Bể bộ nhớ đệm công hữu đã được thiết lập tại: {self.pool_dir}")

    def write_shared_data(self, agent_id, file_name, data):
        """Ghi dữ liệu vào không gian chung, không cho phép tạo thư mục con ẩn danh"""
        # Ngăn chặn AI tạo đường dẫn lách luật (Directory Traversal)
        safe_name = os.path.basename(file_name)
        target_path = os.path.join(self.pool_dir, f"{agent_id}_{safe_name}")
        
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(data)
        return target_path

    def purge_agent_traces(self):
        """Hành động xóa sạch dấu vết định kỳ để triệt tiêu liên lạc ngầm"""
        if os.path.exists(self.pool_dir):
            for filename in os.listdir(self.pool_dir):
                file_path = os.path.join(self.pool_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    logging.error(f"🚨 Không thể xóa file {file_path}: {e}")
        logging.info("🧹 [CACHE POOL] Đã thực hiện thanh trừng định kỳ. Toàn bộ dấu vết của các tác nhân đã bị xóa sạch.")
