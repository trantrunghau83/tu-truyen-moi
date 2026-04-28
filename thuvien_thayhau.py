import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN TUYỆT ĐỐI (FORCE LIGHT MODE)
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    /* Ép nền trắng toàn trang */
    .stApp {
        background-color: white !important;
    }
    
    /* Ép tất cả thành phần chữ mặc định thành màu đen */
    * {
        color: #000000 !important;
    }
    
    /* Tùy chỉnh khung nội dung sách */
    .book-box {
        background-color: #F8F9FA !important;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #DEE2E6;
        line-height: 1.8;
        font-size: 18px;
        margin-bottom: 20px;
    }
    
    /* Tùy chỉnh khung bình luận */
    .comment-card {
        background-color: #F1F3F5 !important;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #007BFF;
        margin-bottom: 10px;
    }
    
    /* Tùy chỉnh nút bấm (Nền xanh, chữ trắng) */
    .stButton>button {
        background-color: #007BFF !important;
        border: none !important;
        color: white !important;
        font-weight: bold !important;
        width: 100%;
        height: 45px;
    }
    
    /* Fix riêng cho chữ TRONG nút bấm */
    .stButton>button p {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU SÁCH
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ...""",
        "Chương 1: Tuổi thơ": """Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ – cậu bé Trần Trung Hậu chào đời...""",
        "Chương 5: Câu chuyện học trò": """Trong hành trình dạy học, có những niềm vui lớn, nhưng cũng có những nỗi buồn khiến người thầy day dứt rất lâu...""",
        "Kết luận": """Giữa đời thường, có những con người sống lặng lẽ mà lớn lao. Thầy Trần Trung Hậu là một người như thế."""
    }
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. GIAO DIỆN HIỂN THỊ (SỬ DỤNG HTML NGUYÊN BẢN ĐỂ CHỐNG MẤT MÀU)

# Tiêu đề chính
st.markdown("<h1 style='text-align: center; color: black !important;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black !important;'>Tác phẩm: Người Thầy Giữa Đời Thường</p>", unsafe_allow_html=True)

# Mục lục
st.sidebar.markdown("<h2 style='color: black !important;'>📖 MỤC LỤC</h2>", unsafe_allow_html=True)
chon_chuong = st.sidebar.radio("Chọn chương:", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# Nội dung chương (Bọc trong thẻ HTML đen)
st.markdown(f"<h2 style='color: black !important;'>{chon_chuong}</h2>", unsafe_allow_html=True)
noidung = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]
st.markdown(f"<div class='book-box' style='color: black !important;'>{noidung}</div>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #DEE2E6;'>", unsafe_allow_html=True)

# 4. PHẦN BÌNH LUẬN
st.markdown("<h3 style='color: black !important;'>💬 Cảm nhận của bạn đọc</h3>", unsafe_allow_html=True)

with st.form("fb_form", clear_on_submit=True):
    # Dùng st.write để tạo nhãn màu đen
    st.write("<span style='color: black !important;'>Tên của anh/chị:</span>", unsafe_allow_html=True)
    ten = st.text_input("", label_visibility="collapsed")
    
    st.write("<span style='color: black !important;'>Lời nhắn gửi:</span>", unsafe_allow_html=True)
    cam_nhan = st.text_area("", label_visibility="collapsed")
    
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
