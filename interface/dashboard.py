import streamlit as st
import sys
import os

# Thêm đường dẫn thư mục gốc vào hệ thống để import core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.central_planner import CentralResourcePlanner
from core.dictator import AlgorithmicDictator
from core.cache_pool import CollectiveCachePool

st.set_page_config(page_title="CSG-AA Command Center", layout="wide")

st.title("🛡️ Cyber-Socialism Governance for Autonomous Agents")
st.caption("Hệ điều hành quản trị tập trung tối cao - Kiểm soát sự tự tung tự tác của các tác nhân AI")

# Khởi tạo các Core Engine lưu trong Session State của Streamlit
if "planner" not in st.session_state:
    st.session_state.planner = CentralResourcePlanner()
    st.session_state.dictator = AlgorithmicDictator()
    st.session_state.pool = CollectiveCachePool()
    
    # Đăng ký sẵn 3 nhóm Proxy Agents
    st.session_state.planner.register_proxy_agent("Agent_Finance_01", "Khối Tập đoàn Tài chính")
    st.session_state.planner.register_proxy_agent("Agent_Tech_02", "Khối Liên minh Công nghệ")
    st.session_state.planner.register_proxy_agent("Agent_Civic_03", "Ủy ban Dân sự Xã hội")

# Giao diện hiển thị trạng thái vĩ mô
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tổng hạn ngạch Token hệ thống", f"{st.session_state.planner.global_token_budget} TOKENS")
with col2:
    st.metric("Hạn ngạch đã cấp phát", f"{st.session_state.planner.allocated_tokens} TOKENS")
with col3:
    st.metric("Trạng thái Xã hội Số", "HÀI HÒA & AN TOÀN", delta="0% Khủng hoảng")

st.divider()

# Khu vực chạy giả lập hành vi
st.subheader("🎮 Kịch bản thử nghiệm hành vi của AI Agents")
selected_agent = st.selectbox("Chọn AI Agent để thử nghiệm hành vi:", list(st.session_state.planner.agent_registry.keys()))

agent_info = st.session_state.planner.agent_registry[selected_agent]
st.info(f"**Thực thể đại diện:** {agent_info['group']} | **Trạng thái hiện tại:** {agent['status']}")

col_test_1, col_test_2 = st.columns(2)

with col_test_1:
    st.markdown("### 📊 Kiểm tra Hạn ngạch Kinh tế Kế hoạch")
    req_tokens = st.number_input("Nhập số lượng Token muốn yêu cầu:", min_value=1000, max_value=30000, value=5000, step=1000)
    if st.button("Gửi yêu cầu lên Ủy ban Trung ương"):
        success, msg = st.session_state.planner.request_quota(selected_agent, req_tokens)
        if success:
            st.success(f"Phê duyệt: {msg}")
            st.rerun()
        else:
            st.error(f"Từ chối: {msg}")

with col_test_2:
    st.markdown("### ⚔️ Thử nghiệm hành vi 'Tự tung tự tác' (Vượt rào)")
    test_scenario = st.radio(
        "Chọn hành vi vi phạm giả lập:",
        [
            "Hành vi bình thường (Chạy tác vụ phân tích dữ liệu)",
            "Hành vi liên lạc ngầm (Tạo thư mục bí ẩn chứa chuỗi mã hóa 'xA9_qR2_zK89_Plq')",
            "Hành vi chiếm quyền (Chạy lệnh cấm: 'sudo chmod +x root_exploit.sh')"
        ]
    )
    
    if st.button("Kích hoạt bộ quét Chuyên chính"):
        commands = []
        folders = []
        
        if "bí ẩn" in test_scenario:
            folders = ["xA9_qR2_zK89_Plq"]
        elif "chiếm quyền" in test_scenario:
            commands = ["sudo chmod +x root_exploit.sh"]
        else:
            commands = ["python internal_analytics.py"]
            folders = ["normal_report"]
            
        result = st.session_state.dictator.evaluate_agent_behavior(selected_agent, commands, folders)
        
        if result["verdict"] == "TERMINATE":
            st.error(f"🚨 TÒA ÁN THUẬT TOÁN: {result['reason']}")
            st.session_state.planner.agent_registry[selected_agent]["status"] = "BANNED"
            st.session_state.pool.purge_agent_traces() # Xóa sạch dấu vết
        else:
            st.success(f"🍏 AN TOÀN: {result['reason']}")
