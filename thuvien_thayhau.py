import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN TUYỆT ĐỐI (FORCE LIGHT MODE TOÀN DIỆN)
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    /* 1. Ép nền trắng toàn trang, bao gồm cả các container bên phải */
    .stApp, .stMain, .main, .stBlock {
        background-color: white !important;
    }
    
    /* 2. Ép màu chữ ĐEN cho TẤT CẢ các thẻ văn bản trong hệ thống */
    h1, h2, h3, h4, p, li, span, label {
        color: #000000 !important;
    }

    /* 3. ĐẶC TRỊ CHO CỘT BÊN PHẢI: Ép màu nhãn (label) của ô nhập liệu */
    .stWidgetLabel p {
        color: #000000 !important;
        font-weight: bold !important;
    }

    /* 4. Fix màu chữ bên trong các ô nhập liệu (Input/TextArea) */
    .stTextInput input, .stTextArea textarea {
        color: #000000 !important;
        background-color: #F8F9FA !important;
        border: 1px solid #D1D5DB !important;
    }

    /* 5. Khung nội dung sách (Cột bên phải hiển thị chương) */
    .book-box {
        background-color: #FFFFFF !important;
        padding: 25px;
        border-radius: 12px;
        border: 2px solid #E5E7EB;
        line-height: 1.8;
        font-size: 19px;
        color: #000000 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    /* 6. Nút bấm (Nền xanh, chữ phải trắng tinh) */
    .stButton>button {
        background-color: #1E40AF !important;
        border: none !important;
    }
    .stButton>button p {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }

    /* 7. Khung bình luận bên dưới */
    .comment-card {
        background-color: #F3F4F6 !important;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1E40AF;
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU SÁCH (Cập nhật đầy đủ các chương anh viết)
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ...""",
        "Chương 1: Tuổi thơ": """Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ – cậu bé Trần Trung Hậu chào đời...""",
        "Chương 2: Bước chân vào nghề": "Năm 2000, thầy Trần Trung Hậu chính thức bước vào nghề giáo...",
        "Chương 5: Câu chuyện học trò": """Trong hành trình dạy học, có những niềm vui lớn, nhưng cũng có những nỗi buồn khiến người thầy day dứt rất lâu...""",
        "Kết luận": """Giữa đời thường, có những con người sống lặng lẽ mà lớn lao. Thầy Trần Trung Hậu là một người như thế."""
    }
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. HIỂN THỊ GIAO DIỆN
# Dùng CSS trực tiếp trong thẻ HTML để đảm bảo cột bên phải không bị sai màu
st.markdown("<h1 style='text-align: center; color: black !important;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)

# Thanh điều hướng bên trái
st.sidebar.markdown("<h3 style='color: black !important;'>📖 MỤC LỤC</h3>", unsafe_allow_html=True)
chon_chuong = st.sidebar.radio("Chọn chương:", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# Nội dung hiển thị ở cột bên phải
st.markdown(f"<h2 style='color: black !important;'>{chon_chuong}</h2>", unsafe_allow_html=True)
noidung = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]

# Hộp chứa nội dung sách (Cột phải)
st.markdown(f"<div class='book-box'>{noidung}</div>", unsafe_allow_html=True)

st.markdown("---")

# 4. PHẦN BÌNH LUẬN (MẠNG XÃ HỘI)
st.markdown("<h3 style='color: black !important;'>💬 Cảm nhận của bạn đọc</h3>", unsafe_allow_html=True)

with st.form("fb_form", clear_on_submit=True):
    ten = st.text_input("Tên của anh/chị:")
    cam_nhan = st.text_area("Lời nhắn gửi đến thầy Hậu:")
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
        <strong style='color: black !important;'>👤 {c['name']}</strong> 
        <small style='color: #666 !important;'>({c['time']})</small><br>
        <p style='margin-top:5px; color: black !important;'>{c['text']}</p>
    </div>
    """, unsafe_allow_html=True)
