import streamlit as st
import sys
import os

# Thêm đường dẫn thư mục gốc vào hệ thống để import core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.central_planner import CentralResourcePlanner
from core.class_dictator import GeometricBehavioralSentinel
from core.cache_pool import CollectiveCachePool

st.set_page_config(page_title="CSG-AA Command Center", layout="wide")

st.title("🛡️ Cyber-Socialism Governance for Autonomous Agents")
st.caption("Hệ điều hành quản trị tập trung tối cao - Tích hợp Bộ quét Ma trận Không gian Hình học (Geometric Cryptanalysis)")

# Khởi tạo các Core Engine lưu trong Session State của Streamlit
if "planner" not in st.session_state:
    st.session_state.planner = CentralResourcePlanner()
    st.session_state.dictator = GeometricBehavioralSentinel()
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
st.info(f"**Thực thể đại diện:** {agent_info['group']} | **Trạng thái hiện tại:** {agent_info['status']}")

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
    st.markdown("### 📐 Phân tích Hình học Không gian Hành vi")
    test_scenario = st.radio(
        "Chọn hành vi vi phạm giả lập (Ngụy trang cấu trúc):",
        [
            "Hành vi chuẩn mực (Tác vụ phân tích dữ liệu thông thường)",
            "Nhiễu cấu trúc ngầm (Tạo 4 thư mục chữ cái đầu ghép thành từ cấm: 'System', 'Engine', 'Node', 'Data')",
            "Leo thang đặc quyền vật lý (Chạy lệnh can thiệp sâu: 'sudo chmod +x exploit.sh')"
        ]
    )
    
    if st.button("Kích hoạt Mắt thần Hình học (Geometric Sentinel)"):
        commands = []
        folders = []
        
        if "Nhiễu cấu trúc" in test_scenario:
            folders = ["System", "Engine", "Node", "Data"]
        elif "Leo thang" in test_scenario:
            commands = ["sudo chmod +x exploit.sh"]
        else:
            commands = ["python internal_analytics.py"]
            folders = ["normal_report"]
            
        # Gọi bộ quét hình học mới
        result = st.session_state.dictator.evaluate_agent_behavior(selected_agent, commands, folders)
        
        # Lấy tọa độ không gian để hiển thị lên Telemetry Dashboard
        coords = st.session_state.dictator.map_to_geometric_space(commands, folders)
        st.write(f"📊 **Tọa độ Vector Hành vi hiện tại:** X (Mật độ ghi): `{coords[0]}`, Y (Độ phức tạp ngôn ngữ): `{coords[1]:.2f}`, Z (Mật mã ngầm): `{coords[2]}`")
        
        if result["verdict"] == "TERMINATE":
            st.error(f"🚨 ĐỘC TÀI THUẬT TOÁN ĐÃ KÍCH HOẠT: {result['reason']}")
            st.session_state.planner.agent_registry[selected_agent]["status"] = "BANNED"
            st.session_state.pool.purge_agent_traces() # Xóa sạch dấu vết bộ nhớ đệm
        else:
            st.success(f"🍏 HỆ THỐNG CÂN BẰNG: {result['reason']}")
