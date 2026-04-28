import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN TUYỆT ĐỐI (TRIỆT TIÊU MÀU TRẮNG)
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    /* Ép nền trắng toàn bộ mọi lớp của Streamlit */
    .stApp, .stMain, .main, [data-testid="stHeader"], [data-testid="stSidebar"] {
        background-color: white !important;
    }
    
    /* Ép tất cả chữ mặc định (label, text) về màu đen */
    * {
        color: #000000 !important;
    }

    /* Khung nội dung sách */
    .book-box {
        background-color: #FFFFFF !important;
        padding: 25px;
        border-radius: 12px;
        border: 2px solid #EEEEEE;
        line-height: 1.8;
        font-size: 19px;
        color: #000000 !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    /* Nút bấm xanh - chữ trắng */
    .stButton>button {
        background-color: #1E40AF !important;
        border: none !important;
    }
    .stButton>button p {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }

    /* Khung bình luận */
    .comment-card {
        background-color: #F9FAFB !important;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1E40AF;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU SÁCH
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ...""",
        "Chương 1: Tuổi thơ": """Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ – cậu bé Trần Trung Hậu chào đời...""",
        "Kết luận": """Giữa đời thường, có những con người sống lặng lẽ mà lớn lao."""
    }
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. HIỂN THỊ GIAO DIỆN (ÉP MÀU TRỰC TIẾP VÀO TỪNG DÒNG)

# Tiêu đề chính (Cột phải) - Ép màu đen trực tiếp
st.markdown("<h1 style='text-align: center; color: #000000 !important; font-weight: bold;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333333 !important;'>Tác phẩm chuyên sâu của Nhà giáo Ưu tú Trần Trung Hậu</p>", unsafe_allow_html=True)

# Sidebar (Cột trái)
st.sidebar.markdown("<h2 style='color: #000000 !important;'>📖 MỤC LỤC</h2>", unsafe_allow_html=True)
chon_chuong = st.sidebar.radio("Chọn chương:", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# Tiêu đề chương (Cột phải) - Ép màu đen trực tiếp
st.markdown(f"<h2 style='color: #000000 !important; border-bottom: 2px solid #1E40AF; padding-bottom: 10px;'>{chon_chuong}</h2>", unsafe_allow_html=True)

# Nội dung chương
noidung = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]
st.markdown(f"<div class='book-box' style='color: #000000 !important;'>{noidung}</div>", unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

# 4. PHẦN BÌNH LUẬN (MẠNG XÃ HỘI)
st.markdown("<h3 style='color: #000000 !important;'>💬 Cảm nhận của bạn đọc</h3>", unsafe_allow_html=True)

with st.form("fb_form", clear_on_submit=True):
    # Nhãn ô nhập liệu ép màu đen
    st.markdown("<p style='margin-bottom: -50px; color: black !important; font-weight: bold;'>Tên của anh/chị:</p>", unsafe_allow_html=True)
    ten = st.text_input("", placeholder="Nhập tên tại đây...")
    
    st.markdown("<p style='margin-bottom: -50px; color: black !important; font-weight: bold;'>Lời nhắn gửi:</p>", unsafe_allow_html=True)
    cam_nhan = st.text_area("", placeholder="Chia sẻ cảm xúc của anh/chị...")
    
    submit = st.form_submit_button("GỬI BÌNH LUẬN")
    
    if submit and ten and cam_nhan:
        st.session_state.comments.insert(0, {
            "name": ten,
            "text": cam_nhan,
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

# Hiển thị bình luận
for c in st.session_state.comments:
    st.markdown(f"""
    <div class='comment-card'>
        <strong style='color: #000000 !important;'>👤 {c['name']}</strong> 
        <small style='color: #666666 !important;'>({c['time']})</small><br>
        <p style='margin-top:5px; color: #000000 !important;'>{c['text']}</p>
    </div>
    """, unsafe_allow_html=True)
