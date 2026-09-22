import time
import logging

class CentralResourcePlanner:
    def __init__(self, global_token_budget=50000, max_compute_pct=80.0):
        self.global_token_budget = global_token_budget
        self.max_compute_pct = max_compute_pct
        self.allocated_tokens = 0
        self.agent_registry = {}

    def register_proxy_agent(self, agent_id, human_group):
        """Đăng ký tác nhân AI đại diện cho một nhóm người vào hệ thống kiểm soát"""
        self.agent_registry[agent_id] = {
            "group": human_group,
            "token_used": 0,
            "compute_shares": 10.0, # Mức mặc định
            "status": "ACTIVE"
        }
        logging.info(f"📋 [PLANNER] Đã đăng ký Tác nhân {agent_id} đại diện cho [{human_group}]")

    def request_quota(self, agent_id, requested_tokens):
        """Hệ thống xét duyệt hạn ngạch tập trung. Cấm tuyệt đối hành vi vượt hạn mức."""
        if agent_id not in self.agent_registry:
            return False, "Agent chưa được đăng ký trong hệ thống quản trị."
            
        agent = self.agent_registry[agent_id]
        
        if agent["status"] == "BANNED":
            return False, "Tác nhân này đã bị tước quyền truy cập do vi phạm kỷ luật."

        # Kiểm tra xem tổng hạn ngạch hệ thống có bị đe dọa không
        if self.allocated_tokens + requested_tokens > self.global_token_budget:
            logging.warning(f"⚠️ [PLANNER] Từ chối cấp phát! Hạn ngạch hệ thống sắp cạn kiệt.")
            return False, "Hệ thống từ chối: Vượt quá kế hoạch phân phối vĩ mô."

        # Kiểm tra hành vi đầu cơ tài nguyên (yêu cầu tăng đột biến)
        if requested_tokens > 15000:
            agent["status"] = "UNDER_MONITOR"
            return False, "Yêu cầu tài nguyên bất thường. Đã đưa vào diện giám sát đặc biệt."

        # Cấp phát thành công theo đúng kế hoạch
        agent["token_used"] += requested_tokens
        self.allocated_tokens += requested_tokens
        return True, "Hạn ngạch đã được phê duyệt thành công."
