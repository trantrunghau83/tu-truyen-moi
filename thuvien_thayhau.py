import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN DARK MODE SANG TRỌNG (CHỐNG LỖI MÀU)
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    /* Ép nền màu xanh đen cực sâu để làm nổi chữ */
    .stApp, .main, [data-testid="stAppViewContainer"] {
        background-color: #0F172A !important;
    }
    
    /* ÉP CHỮ MÀU TRẮNG HOẶC VÀNG NHẠT CHO RÕ NÉT */
    h1, h2, h3, h4, p, span, label, li, div {
        color: #F1F5F9 !important; /* Màu trắng xám dịu mắt */
    }

    /* Tiêu đề chính màu Vàng Kim để nổi bật */
    .main-title {
        color: #FDE047 !important;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* Khung nội dung sách: Nền tối nhẹ, chữ trắng */
    .book-content {
        background-color: #1E293B !important;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #334155;
        line-height: 1.8;
        font-size: 18px;
        color: #F8FAFC !important;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }

    /* Tùy chỉnh Sidebar (Mục lục) */
    [data-testid="stSidebar"] {
        background-color: #1E293B !important;
    }
    [data-testid="stSidebar"] * {
        color: #F1F5F9 !important;
    }

    /* Nút bấm */
    .stButton>button {
        background-color: #3B82F6 !important;
        color: white !important;
        border-radius: 10px !important;
        width: 100%;
    }
    
    /* Ô nhập liệu */
    input, textarea {
        background-color: #334155 !important;
        color: white !important;
        border: 1px solid #475569 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU NỘI DUNG SÁCH
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ...""",
        "Chương 1: Tuổi thơ": """Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ...""",
        "Chương 5: Câu chuyện học trò": """Trong hành trình dạy học, có những niềm vui lớn, nhưng cũng có những nỗi buồn...""",
        "Kết luận": """Giữa đời thường, có những con người sống lặng lẽ mà lớn lao."""
    }
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. HIỂN THỊ CỘT PHẢI

# Tiêu đề chính
st.markdown("<p class='main-title'>📚 THƯ VIỆN SỐ THẦY HẬU</p>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #94A3B8;'>Tác phẩm của Nhà giáo Ưu tú Trần Trung Hậu</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("### 📖 MỤC LỤC")
chon_chuong = st.sidebar.radio("Chọn chương:", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# Nội dung chương ở cột phải
st.markdown(f"<h2 style='color: #FDE047 !important;'>{chon_chuong}</h2>", unsafe_allow_html=True)
noidung = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]

st.markdown(f"""
    <div class='book-content'>
        {noidung}
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: #334155;'>", unsafe_allow_html=True)

# 4. PHẦN BÌNH LUẬN
st.subheader("💬 Cảm nhận của bạn đọc")

with st.form("comment_form", clear_on_submit=True):
    ten = st.text_input("Tên của bạn:")
    bl = st.text_area("Lời nhắn gửi:")
    gui = st.form_submit_button("GỬI BÌNH LUẬN")
    
    if gui and ten and bl:
        st.session_state.comments.insert(0, {
            "name": ten, "text": bl, "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

# Hiển thị bình luận
for c in st.session_state.comments:
    st.markdown(f"""
    <div style='background-color: #1E293B; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid #3B82F6;'>
        <strong style='color: #FDE047;'>👤 {c['name']}</strong> <small style='color: #94A3B8;'>({c['time']})</small><br>
        <p style='margin-top:5px;'>{c['text']}</p>
    </div>
    """, unsafe_allow_html=True)
