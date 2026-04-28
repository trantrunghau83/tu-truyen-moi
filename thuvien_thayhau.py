import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN (BLOCK DARK MODE)
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    /* Ép nền trắng cho toàn bộ các lớp của Streamlit */
    .stApp, .stMain, .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
    }
    
    /* ÉP MÀU ĐEN CHO TẤT CẢ CÁC THÀNH PHẦN CHỮ */
    h1, h2, h3, h4, p, span, label, div, small, .stMarkdown {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important; /* Lệnh ép màu cho trình duyệt Safari/iPhone */
    }

    /* Khung nội dung trắng tinh chữ đen */
    .book-container {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        padding: 20px;
        border: 2px solid #EEEEEE;
        border-radius: 10px;
    }

    /* Ép màu cho nhãn của các ô nhập liệu bên phải */
    .stWidgetLabel p, [data-testid="stMarkdownContainer"] p {
        color: #000000 !important;
    }

    /* Nút bấm giữ màu xanh, chữ trắng */
    .stButton>button {
        background-color: #1E40AF !important;
        color: white !important;
    }
    .stButton>button p {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU SÁCH
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": "Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ...",
        "Chương 1: Tuổi thơ": "Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ...",
        "Kết luận": "Giữa đời thường, có những con người sống lặng lẽ mà lớn lao."
    }
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. HIỂN THỊ CỘT PHẢI (DÙNG HTML TRỰC TIẾP)

# TIÊU ĐỀ CHÍNH
st.markdown("<div style='all: unset; display: block; text-align: center;'><h1 style='color: black !important; -webkit-text-fill-color: black !important;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1></div>", unsafe_allow_html=True)
st.markdown("<div style='all: unset; display: block; text-align: center;'><p style='color: black !important;'>Tác phẩm của Nhà giáo Ưu tú Trần Trung Hậu</p></div>", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.markdown("<h2 style='color: black !important;'>📖 MỤC LỤC</h2>", unsafe_allow_html=True)
chon_chuong = st.sidebar.radio("", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# TIÊU ĐỀ CHƯƠNG VÀ NỘI DUNG (CỘT PHẢI)
st.markdown(f"<div style='all: unset; display: block; border-bottom: 2px solid blue;'><h2 style='color: black !important; -webkit-text-fill-color: black !important;'>{chon_chuong}</h2></div>", unsafe_allow_html=True)

noidung = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]
st.markdown(f"""
    <div class='book-container'>
        <p style='color: black !important; -webkit-text-fill-color: black !important; font-size: 18px;'>
            {noidung}
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 4. PHẦN BÌNH LUẬN
st.markdown("<h3 style='color: black !important;'>💬 Cảm nhận bạn đọc</h3>", unsafe_allow_html=True)

with st.form("fb_form"):
    st.markdown("<p style='color: black !important; font-weight: bold;'>Tên của bạn:</p>", unsafe_allow_html=True)
    ten = st.text_input("", label_visibility="collapsed")
    
    st.markdown("<p style='color: black !important; font-weight: bold;'>Lời nhắn:</p>", unsafe_allow_html=True)
    cam_nhan = st.text_area("", label_visibility="collapsed")
    
    submit = st.form_submit_button("Gửi")
    if submit and ten and cam_nhan:
        st.session_state.comments.insert(0, {"name": ten, "text": cam_nhan, "time": datetime.now().strftime("%d/%m/%Y")})
        st.rerun()

for c in st.session_state.comments:
    st.markdown(f"""
        <div style='background-color: #F0F2F6; padding: 10px; border-radius: 5px; margin-bottom: 5px;'>
            <strong style='color: black !important;'>{c['name']}</strong> <small style='color: gray;'>({c['time']})</small><br>
            <p style='color: black !important;'>{c['text']}</p>
        </div>
    """, unsafe_allow_html=True)
