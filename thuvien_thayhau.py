import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN TUYỆT ĐỐI (FORCE LIGHT MODE)
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

# Lệnh CSS này để quét sạch các khoảng trắng dư thừa và ép nền trắng
st.markdown("""
    <style>
    /* Ép nền trắng tuyệt đối cho mọi ngóc ngách */
    [data-testid="stAppViewContainer"], .main, .stApp, [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
    }
    /* Ẩn các thành phần thừa của Streamlit có thể gây màu trắng */
    header, footer {visibility: hidden;}
    
    /* Khung nội dung sách */
    .book-box {
        background-color: #FDFDFD !important;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #EEEEEE;
        line-height: 1.8;
        font-size: 19px;
        color: #000000 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-top: 10px;
    }
    
    /* Nút bấm xanh chữ trắng */
    .stButton>button {
        background-color: #1E40AF !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
    }
    
    /* Khung bình luận */
    .comment-card {
        background-color: #F3F4F6 !important;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #1E40AF;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU NỘI DUNG SÁCH
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ...""",
        "Chương 1: Tuổi thơ": """Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ – cậu bé Trần Trung Hậu chào đời...""",
        "Kết luận": """Giữa đời thường, có những con người sống lặng lẽ mà lớn lao. Thầy Trần Trung Hậu là một người như thế."""
    }
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. HIỂN THỊ GIAO DIỆN (DÙNG HTML THUẦN ĐỂ ÉP MÀU ĐEN)

# Tiêu đề chính (Dùng HTML để không bị Streamlit can thiệp)
st.markdown("<div style='text-align: center;'><span style='color: #000000 !important; font-size: 35px; font-weight: bold;'>📚 THƯ VIỆN SỐ THẦY HẬU</span></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'><span style='color: #444444 !important; font-size: 18px;'>Tác phẩm chuyên sâu của Nhà giáo Ưu tú Trần Trung Hậu</span></div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Sidebar (Mục lục)
st.sidebar.markdown("<span style='color: #000000 !important; font-size: 24px; font-weight: bold;'>📖 MỤC LỤC</span>", unsafe_allow_html=True)
chon_chuong = st.sidebar.radio("", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# Tiêu đề chương và Nội dung (ÉP MÀU ĐEN TRỰC TIẾP TRONG THẺ SPAN)
st.markdown(f"<div style='border-bottom: 2px solid #1E40AF; padding-bottom: 5px;'><span style='color: #000000 !important; font-size: 26px; font-weight: bold;'>{chon_chuong}</span></div>", unsafe_allow_html=True)

noidung = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]
st.markdown(f"<div class='book-box'><span style='color: #000000 !important;'>{noidung}</span></div>", unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

# 4. PHẦN BÌNH LUẬN
st.markdown("<span style='color: #000000 !important; font-size: 22px; font-weight: bold;'>💬 Cảm nhận của bạn đọc</span>", unsafe_allow_html=True)

with st.form("fb_form", clear_on_submit=True):
    st.markdown("<span style='color: #000000 !important; font-weight: bold;'>Tên của anh/chị:</span>", unsafe_allow_html=True)
    ten = st.text_input("", label_visibility="collapsed")
    
    st.markdown("<span style='color: #000000 !important; font-weight: bold;'>Lời nhắn gửi:</span>", unsafe_allow_html=True)
    cam_nhan = st.text_area("", label_visibility="collapsed")
    
    submit = st.form_submit_button("GỬI BÌNH LUẬN")
    
    if submit and ten and cam_nhan:
        st.session_state.comments.insert(0, {
            "name": ten,
            "text": cam_nhan,
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

# Hiển thị bình luận (Sử dụng span màu đen)
for c in st.session_state.comments:
    st.markdown(f"""
    <div class='comment-card'>
        <span style='color: #000000 !important; font-weight: bold;'>👤 {c['name']}</span> 
        <span style='color: #666666 !important; font-size: 12px;'>({c['time']})</span><br>
        <div style='margin-top:8px;'><span style='color: #000000 !important;'>{c['text']}</span></div>
    </div>
    """, unsafe_allow_html=True)
