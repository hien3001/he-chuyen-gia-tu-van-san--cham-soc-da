# -*- coding: utf-8 -*-
"""
HỆ CHUYÊN GIA TƯ VẤN SẢN PHẨM CHĂM SÓC DA MẶT CƠ BẢN
Dữ liệu sản phẩm được tổng hợp từ báo cáo NHÓM 13.docx.
Giao diện web: Streamlit.
"""

from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Hệ chuyên gia tư vấn sản phẩm chăm sóc da",
    page_icon="🌿",
    layout="wide"
)


# ==========================================================
# GIAO DIỆN NÂNG CẤP – SKINCARE PREMIUM
# Chỉ bổ sung CSS, không thay đổi dữ liệu và logic xử lý.
# ==========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

:root {
    --ink: #24364b;
    --muted: #718096;
    --mint: #8edbc9;
    --lavender: #c5b8f4;
    --pink: #f3bfd5;
    --line: rgba(143, 169, 190, .25);
}

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 8% 4%, rgba(190, 239, 226, .62), transparent 31%),
        radial-gradient(ellipse at 95% 9%, rgba(226, 207, 250, .58), transparent 30%),
        radial-gradient(ellipse at 80% 88%, rgba(255, 220, 231, .42), transparent 28%),
        linear-gradient(135deg, #f7fcfb 0%, #f8f7ff 48%, #fff8fb 100%);
    color: var(--ink);
}

[data-testid="stHeader"] {
    background: rgba(255,255,255,0);
}

[data-testid="stAppViewContainer"] > .main {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

h1 {
    font-weight: 800 !important;
    letter-spacing: -1.2px !important;
    line-height: 1.35 !important;
    background: linear-gradient(100deg, #168d83 0%, #6d78c9 48%, #cf79a7 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    text-align: center;
    padding: 14px 8px 5px;
    filter: drop-shadow(0 5px 12px rgba(113, 139, 177, .12));
}

h2, h3 {
    color: #344b62 !important;
    font-weight: 750 !important;
    letter-spacing: -.35px;
}

[data-testid="stCaptionContainer"] {
    color: #8293a5;
    text-align: center;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, .76);
    border: 1px solid rgba(255, 255, 255, .92) !important;
    border-radius: 23px !important;
    box-shadow: 0 12px 35px rgba(76, 105, 130, .09);
    backdrop-filter: blur(14px);
    padding: 8px 10px;
    transition: transform .25s ease, box-shadow .25s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    box-shadow: 0 16px 38px rgba(104, 127, 164, .15);
    transform: translateY(-2px);
}

[data-testid="stWidgetLabel"] p {
    color: #435b70 !important;
    font-weight: 650 !important;
    font-size: .94rem !important;
}

div[data-baseweb="select"] > div {
    background: rgba(255,255,255,.94) !important;
    border: 1px solid #dce9eb !important;
    border-radius: 13px !important;
    min-height: 45px;
    box-shadow: 0 3px 10px rgba(91, 132, 143, .045);
    transition: border-color .2s ease, box-shadow .2s ease;
}

div[data-baseweb="select"] > div:hover {
    border-color: #8bcfc2 !important;
    box-shadow: 0 0 0 3px rgba(139, 207, 194, .13);
}

div[data-baseweb="popover"] {
    border-radius: 14px !important;
    overflow: hidden;
}

.stButton > button {
    border: 0 !important;
    border-radius: 15px !important;
    min-height: 49px;
    padding: 10px 25px !important;
    color: white !important;
    font-weight: 750 !important;
    letter-spacing: .2px;
    background: linear-gradient(105deg, #36b7a4 0%, #718bd6 55%, #b47bc8 100%) !important;
    box-shadow: 0 9px 22px rgba(105, 139, 190, .25);
    transition: all .25s ease !important;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 13px 27px rgba(105, 139, 190, .34);
    filter: brightness(1.06);
}

.stButton > button:active {
    transform: translateY(0);
}

[data-testid="stAlert"] {
    border-radius: 16px !important;
    border: 1px solid rgba(155, 190, 194, .22) !important;
    box-shadow: 0 5px 16px rgba(93, 126, 145, .06);
}

[data-testid="stImage"] img {
    border-radius: 17px;
    box-shadow: 0 8px 22px rgba(67, 91, 119, .12);
    object-fit: contain;
    background: #fff;
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #b8dcd8, #d8c5ed, transparent);
    margin: 1.7rem 0;
}

.stMarkdown p, .stMarkdown li {
    line-height: 1.75;
    color: #526579;
}

.stMarkdown strong {
    color: #315e69;
}

[data-testid="stMetric"] {
    background: rgba(255,255,255,.72);
    border: 1px solid rgba(198, 220, 220, .55);
    border-radius: 17px;
    padding: 14px 17px;
}

footer {
    visibility: hidden;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem .8rem 2rem;
    }
    h1 {
        font-size: 1.65rem !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 17px !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================================
# 1. CƠ SỞ TRI THỨC
# Mã sản phẩm S1-S40, nhóm L, thương hiệu H, loại da D,
# dung tích T và giá G bám theo bảng mã trong báo cáo.
# ==========================================================
PRODUCTS = [
    {
        "id": "S1",
        "name": "Nước tẩy trang Bioderma Sensibio H2O",
        "type": "Nước tẩy trang",
        "brand": "Bioderma",
        "skin_types": [
            "Da khô",
            "Da nhạy cảm"
        ],
        "description": "Nước tẩy trang giúp làm sạch bụi bẩn và lớp trang điểm trên mặt, kể cả vùng mắt, phù hợp với da nhạy cảm.",
        "variants": [
            {
                "size": 100.0,
                "unit": "ml",
                "price": 180000
            },
            {
                "size": 250.0,
                "unit": "ml",
                "price": 320000
            },
            {
                "size": 500.0,
                "unit": "ml",
                "price": 440000
            }
        ],
        "brand_code": "H1",
        "type_code": "L1"
    },
    {
        "id": "S2",
        "name": "Nước tẩy trang Garnier Micellar Cleansing Water",
        "type": "Nước tẩy trang",
        "brand": "Garnier",
        "skin_types": [
            "Da thường",
            "Da nhạy cảm"
        ],
        "description": "Nước tẩy trang giúp loại bỏ lớp trang điểm nhẹ, kem chống nắng và bụi bẩn, phù hợp da khô, da nhạy cảm.",
        "variants": [
            {
                "size": 400.0,
                "unit": "ml",
                "price": 170000
            },
            {
                "size": 700.0,
                "unit": "ml",
                "price": 190000
            }
        ],
        "brand_code": "H2",
        "type_code": "L1"
    },
    {
        "id": "S3",
        "name": "Nước tẩy trang L'Oréal Paris Micellar Water 3-in-1",
        "type": "Nước tẩy trang",
        "brand": "L'Oréal Paris",
        "skin_types": [
            "Da dầu",
            "Da hỗn hợp",
            "Da đang điều trị"
        ],
        "description": "Nước tẩy trang giúp loại bỏ bụi bẩn và lớp trang điểm, đồng thời làm mát và dưỡng ẩm cho da, phù hợp với da dầu, da hỗn hợp và da nhạy cảm.",
        "variants": [
            {
                "size": 400.0,
                "unit": "ml",
                "price": 150000
            }
        ],
        "brand_code": "H3",
        "type_code": "L1"
    },
    {
        "id": "S4",
        "name": "Nước tẩy trang Simple Kind to Skin Micellar Cleansing Water",
        "type": "Nước tẩy trang",
        "brand": "Simple",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da nhạy cảm"
        ],
        "description": "Nước tẩy trang giúp loại bỏ bụi bẩn, lớp trang điểm và tạp chất, đồng thời hỗ trợ dưỡng ẩm và làm dịu da, phù hợp với da nhạy cảm.",
        "variants": [
            {
                "size": 400.0,
                "unit": "ml",
                "price": 150000
            }
        ],
        "brand_code": "H4",
        "type_code": "L1"
    },
    {
        "id": "S5",
        "name": "Nước tẩy trang La Roche-Posay Micellar Water Ultra",
        "type": "Nước tẩy trang",
        "brand": "La Roche-Posay",
        "skin_types": [
            "Da nhạy cảm"
        ],
        "description": "Nước tẩy trang giúp loại bỏ lớp trang điểm, bã nhờn và bụi bẩn, đồng thời dưỡng ẩm và làm dịu da, phù hợp với da nhạy cảm.",
        "variants": [
            {
                "size": 200.0,
                "unit": "ml",
                "price": 290000
            },
            {
                "size": 400.0,
                "unit": "ml",
                "price": 360000
            }
        ],
        "brand_code": "H5",
        "type_code": "L1"
    },
    {
        "id": "S6",
        "name": "Nước tẩy trang Garnier Micellar Oil-Infused Cleansing Water",
        "type": "Nước tẩy trang",
        "brand": "Garnier",
        "skin_types": [
            "Da khô"
        ],
        "description": "Nước tẩy trang giúp loại bỏ lớp trang điểm lâu trôi và mỹ phẩm chống nước, cần lắc đều trước khi sử dụng.",
        "variants": [
            {
                "size": 400.0,
                "unit": "ml",
                "price": 140000
            }
        ],
        "brand_code": "H2",
        "type_code": "L1"
    },
    {
        "id": "S7",
        "name": "Nước tẩy trang Bioderma Sébium H2O",
        "type": "Nước tẩy trang",
        "brand": "Bioderma",
        "skin_types": [
            "Da dầu",
            "Da hỗn hợp",
            "Da mụn"
        ],
        "description": "Nước tẩy trang giúp làm sạch dầu thừa và bụi bẩn, phù hợp với da dầu và da hỗn hợp thiên dầu.",
        "variants": [
            {
                "size": 100.0,
                "unit": "ml",
                "price": 180000
            },
            {
                "size": 250.0,
                "unit": "ml",
                "price": 320000
            },
            {
                "size": 500.0,
                "unit": "ml",
                "price": 440000
            }
        ],
        "brand_code": "H1",
        "type_code": "L1"
    },
    {
        "id": "S8",
        "name": "Nước tẩy trang L'Oréal Paris Hyaluronic Acid Hydrating Micellar Water",
        "type": "Nước tẩy trang",
        "brand": "L'Oréal Paris",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da đang điều trị"
        ],
        "description": "Nước tẩy trang giúp loại bỏ bụi bẩn, kem chống nắng và lớp trang điểm, đồng thời cấp ẩm cho da nhờ Hyaluronic Acid (HA), phù hợp với da khô, da hỗn hợp và da nhạy cảm.",
        "variants": [
            {
                "size": 400.0,
                "unit": "ml",
                "price": 170000
            }
        ],
        "brand_code": "H3",
        "type_code": "L1"
    },
    {
        "id": "S9",
        "name": "Nước tẩy trang bí đao Cocoon",
        "type": "Nước tẩy trang",
        "brand": "Cocoon",
        "skin_types": [
            "Da dầu",
            "Da hỗn hợp",
            "Da mụn"
        ],
        "description": "Nước tẩy trang ứng dụng công nghệ Micellar, giúp loại bỏ bụi bẩn, lớp trang điểm và dầu thừa, hỗ trợ làm sạch da dầu mụn.",
        "variants": [
            {
                "size": 140.0,
                "unit": "ml",
                "price": 100000
            },
            {
                "size": 500.0,
                "unit": "ml",
                "price": 250000
            },
            {
                "size": 1000.0,
                "unit": "ml",
                "price": 350000
            }
        ],
        "brand_code": "H6",
        "type_code": "L1"
    },
    {
        "id": "S10",
        "name": "Nước tẩy trang Dr.Ceutics Ultra-Mild Olive Cleansing Water",
        "type": "Nước tẩy trang",
        "brand": "Dr.Ceutics",
        "skin_types": [
            "Da khô",
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Nước tẩy trang chiết xuất olive, giúp loại bỏ bụi bẩn, dầu thừa và lớp trang điểm, hỗ trợ làm sạch da dịu nhẹ.",
        "variants": [
            {
                "size": 310.0,
                "unit": "ml",
                "price": 100000
            },
            {
                "size": 500.0,
                "unit": "ml",
                "price": 160000
            }
        ],
        "brand_code": "H7",
        "type_code": "L1"
    },
    {
        "id": "S11",
        "name": "Sữa rửa mặt Cetaphil Gentle Skin Cleanser",
        "type": "Sữa rửa mặt",
        "brand": "Cetaphil",
        "skin_types": [
            "Da nhạy cảm",
            "Da đang điều trị",
            "Da mụn"
        ],
        "description": "Sữa rửa mặt giúp làm sạch bụi bẩn và tạp chất, đồng thời dưỡng ẩm, làm dịu da và hỗ trợ bảo vệ hàng rào da, phù hợp với mọi loại da, đặc biệt là da nhạy cảm.",
        "variants": [
            {
                "size": 118.0,
                "unit": "ml",
                "price": 160000
            },
            {
                "size": 236.0,
                "unit": "ml",
                "price": 290000
            },
            {
                "size": 473.0,
                "unit": "ml",
                "price": 360000
            },
            {
                "size": 1000.0,
                "unit": "ml",
                "price": 630000
            }
        ],
        "brand_code": "H8",
        "type_code": "L2"
    },
    {
        "id": "S12",
        "name": "Sữa rửa mặt CeraVe Foaming Facial Cleanser",
        "type": "Sữa rửa mặt",
        "brand": "CeraVe",
        "skin_types": [
            "Da thường",
            "Da dầu"
        ],
        "description": "Sữa rửa mặt giúp làm sạch dầu thừa và bụi bẩn, chứa ceramide và niacinamide giúp hỗ trợ bảo vệ da, phù hợp với da thường đến da dầu.",
        "variants": [
            {
                "size": 88.0,
                "unit": "ml",
                "price": 140000
            },
            {
                "size": 236.0,
                "unit": "ml",
                "price": 280000
            },
            {
                "size": 473.0,
                "unit": "ml",
                "price": 380000
            }
        ],
        "brand_code": "H9",
        "type_code": "L2"
    },
    {
        "id": "S13",
        "name": "Gel rửa mặt La Roche-Posay Effaclar Purifying Foaming Gel",
        "type": "Sữa rửa mặt",
        "brand": "La Roche-Posay",
        "skin_types": [
            "Da dầu",
            "Da nhạy cảm"
        ],
        "description": "Gel rửa mặt giúp làm sạch bụi bẩn, bã nhờn và hỗ trợ giảm mụn, chứa Zinc PCA giúp kiểm soát dầu và nước khoáng giúp làm dịu da, phù hợp với da dầu, da mụn và da nhạy cảm.",
        "variants": [
            {
                "size": 200.0,
                "unit": "ml",
                "price": 340000
            },
            {
                "size": 400.0,
                "unit": "ml",
                "price": 420000
            }
        ],
        "brand_code": "H5",
        "type_code": "L2"
    },
    {
        "id": "S14",
        "name": "Gel rửa mặt Simple Kind to Skin Refreshing Facial Wash",
        "type": "Sữa rửa mặt",
        "brand": "Simple",
        "skin_types": [
            "Da nhạy cảm"
        ],
        "description": "Gel rửa mặt giúp làm sạch bụi bẩn, bã nhờn, chứa vitamin B5, vitamin E và chiết xuất hoa cúc La Mã, có độ pH 5, phù hợp với da nhạy cảm.",
        "variants": [
            {
                "size": 150.0,
                "unit": "ml",
                "price": 130000
            }
        ],
        "brand_code": "H4",
        "type_code": "L2"
    },
    {
        "id": "S15",
        "name": "Sữa rửa mặt Hada Labo Advanced Nourish Cleanser",
        "type": "Sữa rửa mặt",
        "brand": "Hada Labo",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Sữa rửa mặt giúp làm sạch bụi bẩn, bã nhờn và tế bào chết, đồng thời bổ sung độ ẩm cho da nhờ HA, SHA và Nano HA, phù hợp với da khô và thiếu ẩm.",
        "variants": [
            {
                "size": 80.0,
                "unit": "g",
                "price": 80000
            }
        ],
        "brand_code": "H10",
        "type_code": "L2"
    },
    {
        "id": "S16",
        "name": "Sữa rửa mặt CeraVe Hydrating Cleanser",
        "type": "Sữa rửa mặt",
        "brand": "CeraVe",
        "skin_types": [
            "Da thường",
            "Da khô"
        ],
        "description": "Sữa rửa mặt giúp làm sạch bụi bẩn và dầu thừa mà không gây khô da, hỗ trợ duy trì độ ẩm và hàng rào bảo vệ da, không gây bít tắc lỗ chân lông, phù hợp với da thường đến da khô.",
        "variants": [
            {
                "size": 88.0,
                "unit": "ml",
                "price": 130000
            },
            {
                "size": 236.0,
                "unit": "ml",
                "price": 280000
            },
            {
                "size": 473.0,
                "unit": "ml",
                "price": 380000
            }
        ],
        "brand_code": "H9",
        "type_code": "L2"
    },
    {
        "id": "S17",
        "name": "Gel rửa mặt SVR sebiaclear Gel Moussant",
        "type": "Sữa rửa mặt",
        "brand": "SVR",
        "skin_types": [
            "Da dầu",
            "Da nhạy cảm",
            "Da mụn"
        ],
        "description": "Gel rửa mặt giúp làm sạch sâu bụi bẩn, bã nhờn và hỗ trợ làm thông thoáng lỗ chân lông. Sản phẩm hướng đến việc làm sạch dịu nhẹ, hỗ trợ giảm mụn và hạn chế các khuyết điểm trên da.",
        "variants": [
            {
                "size": 55.0,
                "unit": "ml",
                "price": 150000
            },
            {
                "size": 200.0,
                "unit": "ml",
                "price": 350000
            },
            {
                "size": 400.0,
                "unit": "ml",
                "price": 430000
            }
        ],
        "brand_code": "H11",
        "type_code": "L2"
    },
    {
        "id": "S18",
        "name": "Gel rửa mặt Bioderma Sébium Gel Moussant",
        "type": "Sữa rửa mặt",
        "brand": "Bioderma",
        "skin_types": [
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Gel rửa mặt không chứa xà phòng, giúp làm sạch bụi bẩn, bã nhờn và kiểm soát dầu thừa, phù hợp với da dầu và da hỗn hợp.",
        "variants": [
            {
                "size": 45.0,
                "unit": "ml",
                "price": 130000
            },
            {
                "size": 200.0,
                "unit": "ml",
                "price": 240000
            },
            {
                "size": 400.0,
                "unit": "ml",
                "price": 370000
            }
        ],
        "brand_code": "H1",
        "type_code": "L2"
    },
    {
        "id": "S19",
        "name": "Gel rửa mặt Eucerin ProACNE Solution Cleansing Gel",
        "type": "Sữa rửa mặt",
        "brand": "Eucerin",
        "skin_types": [
            "Da dầu",
            "Da nhạy cảm",
            "Da mụn"
        ],
        "description": "Gel rửa mặt có công thức dịu nhẹ, giúp làm sạch bụi bẩn và dầu thừa mà không gây khô da, phù hợp với da nhạy cảm.",
        "variants": [
            {
                "size": 200.0,
                "unit": "ml",
                "price": 340000
            }
        ],
        "brand_code": "H12",
        "type_code": "L2"
    },
    {
        "id": "S20",
        "name": "Gel rửa mặt Gel bí đao rửa mặt Cocoon",
        "type": "Sữa rửa mặt",
        "brand": "Cocoon",
        "skin_types": [
            "Da dầu",
            "Da hỗn hợp",
            "Da mụn"
        ],
        "description": "Gel rửa mặt giúp làm sạch bụi bẩn, dầu thừa, hỗ trợ giảm mụn và duy trì độ ẩm cho da.",
        "variants": [
            {
                "size": 140.0,
                "unit": "ml",
                "price": 140000
            },
            {
                "size": 310.0,
                "unit": "ml",
                "price": 250000
            },
            {
                "size": 500.0,
                "unit": "ml",
                "price": 300000
            }
        ],
        "brand_code": "H6",
        "type_code": "L2"
    },
    {
        "id": "S21",
        "name": "Kem dưỡng làm dịu da DIVE IN",
        "type": "Kem dưỡng",
        "brand": "Torriden",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da hỗn hợp",
            "Da nhạy cảm"
        ],
        "description": "Torriden DIVE IN Soothing Cream là kem dưỡng da đến từ thương hiệu mỹ phẩm Hàn Quốc Torriden, thuộc dòng DIVE IN nổi tiếng với thành phần cấp ẩm Hyaluronic Acid. Sản phẩm hướng đến việc cấp nước, làm dịu da và hỗ trợ duy trì hàng rào bảo vệ da. Nếu da đang nhạy cảm hoặc dễ nổi mụn, hãy thử sản phẩm trên một vùng da nhỏ trước khi dùng toàn mặt. Kem dưỡng giúp cấp ẩm và làm dịu da nhưng không phải thuốc điều trị mụn hay các bệnh lý da liễu.",
        "variants": [
            {
                "size": 100.0,
                "unit": "ml",
                "price": 320000
            }
        ],
        "brand_code": "H13",
        "type_code": "L3"
    },
    {
        "id": "S22",
        "name": "Kem dưỡng ẩm cấp nước Neutrogena® Hydro Boost Hyaluronic Acid Water Gel",
        "type": "Kem dưỡng",
        "brand": "Neutrogena",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da nhạy cảm"
        ],
        "description": "Neutrogena® Hydro Boost Hyaluronic Acid Water Gel là kem dưỡng ẩm dạng gel, được phát triển với sự tham vấn của chuyên gia da liễu, giúp cấp nước và duy trì độ ẩm cho làn da. Sản phẩm ứng dụng Hyaluronic Acid kết hợp với phức hợp NMF (Natural Moisturizing Factor), hỗ trợ tăng cường khả năng giữ ẩm tự nhiên, giúp da mềm mại, căng mịn và tươi tắn hơn. Bên cạnh đó, Amino Acid hỗ trợ hàng rào bảo vệ da, hạn chế tình trạng thất thoát độ ẩm, trong khi chất điện giải góp phần hỗ trợ quá trình duy trì độ ẩm của da. Với kết cấu gel mát nhẹ, thấm nhanh và ít gây cảm giác nhờn rít, sản phẩm phù hợp để sử dụng hằng ngày, giúp làn da duy trì trạng thái ẩm mượt và dễ chịu. Công thức không chứa cồn khô, phthalates và phẩm màu theo thông tin sản phẩm được cung cấp.",
        "variants": [
            {
                "size": 15.0,
                "unit": "g",
                "price": 104000
            },
            {
                "size": 50.0,
                "unit": "g",
                "price": 315000
            }
        ],
        "brand_code": "H14",
        "type_code": "L3"
    },
    {
        "id": "S23",
        "name": "Kem dưỡng giúp phục hồi da Caryophy",
        "type": "Kem dưỡng",
        "brand": "Caryophy",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da nhạy cảm"
        ],
        "description": "Kem dưỡng phục hồi da Caryophy là sản phẩm chăm sóc da thuộc thương hiệu Caryophy của Hàn Quốc, được hướng đến việc dưỡng ẩm, làm dịu và hỗ trợ phục hồi làn da. Sản phẩm giúp bổ sung độ ẩm cần thiết, hạn chế tình trạng da khô ráp, đồng thời hỗ trợ duy trì hàng rào bảo vệ da, giúp da mềm mại và khỏe mạnh hơn. Kem dưỡng có thể được sử dụng trong chu trình chăm sóc da hằng ngày, đặc biệt khi da cần được cấp ẩm và chăm sóc sau các bước làm sạch. Tùy theo từng dòng sản phẩm, công thức và công dụng cụ thể có thể khác nhau; người dùng nên kiểm tra thành phần trên bao bì để lựa chọn sản phẩm phù hợp với tình trạng da của mình.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 425000
            }
        ],
        "brand_code": "H15",
        "type_code": "L3"
    },
    {
        "id": "S24",
        "name": "Kem dưỡng da Beplain Cica PDRN Repair Cream",
        "type": "Kem dưỡng",
        "brand": "Beplain",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da hỗn hợp",
            "Da nhạy cảm",
            "Da đang điều trị"
        ],
        "description": "Beplain Cica PDRN Repair Cream – Kem Dưỡng Phục Hồi Da Chuyên Sâu & Làm Dịu Da Nhạy Cảm. Beplain Cica PDRN Repair Cream là kem dưỡng phục hồi đến từ Hàn Quốc, được phát triển dành cho làn da nhạy cảm, da yếu hoặc đang trong quá trình treatment. Công thức kết hợp PDRN (Sodium DNA), chiết xuất Rau Má (Cica), Peptide, Ceramide và Hyaluronic Acid giúp hỗ trợ làm dịu da, cấp ẩm chuyên sâu, củng cố hàng rào bảo vệ da và cải thiện độ đàn hồi, mang lại làn da khỏe mạnh, mềm mịn và căng bóng.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 420000
            }
        ],
        "brand_code": "H16",
        "type_code": "L3"
    },
    {
        "id": "S25",
        "name": "Kem dưỡng ẩm CERAVE MOISTURISING CREAM",
        "type": "Kem dưỡng",
        "brand": "CeraVe",
        "skin_types": [
            "Da thường"
        ],
        "description": "CeraVe Moisturizing Cream là kem dưỡng ẩm được thiết kế dành cho da mặt và toàn thân, giúp bổ sung độ ẩm, hạn chế tình trạng mất nước và hỗ trợ phục hồi hàng rào bảo vệ tự nhiên của da. Sản phẩm nổi bật với sự kết hợp của 3 loại Ceramides thiết yếu (Ceramide 1, 3 và 6-II) cùng Hyaluronic Acid, giúp duy trì độ ẩm, cải thiện tình trạng da khô ráp và mang lại cảm giác mềm mại, mịn màng. Bên cạnh đó, công nghệ phân phối dưỡng chất MVE (MultiVesicular Emulsion) giúp giải phóng các thành phần dưỡng ẩm từ từ, hỗ trợ duy trì độ ẩm trong thời gian dài. Với công thức tập trung vào việc dưỡng ẩm và củng cố hàng rào bảo vệ da, sản phẩm phù hợp để sử dụng hằng ngày, đặc biệt đối với làn da khô, thiếu ẩm hoặc cần được chăm sóc để duy trì trạng thái khỏe mạnh.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 172000
            }
        ],
        "brand_code": "H9",
        "type_code": "L3"
    },
    {
        "id": "S26",
        "name": "Thạch hoa hồng dưỡng ẩm (kem dưỡng ẩm) Cocoon",
        "type": "Kem dưỡng",
        "brand": "Cocoon",
        "skin_types": [
            "Da khô"
        ],
        "description": "Thạch dưỡng ẩm hoa hồng phiên bản BIG SIZE 100ml mang đến giải pháp chăm sóc da tiện lợi và tiết kiệm hơn. Sản phẩm sở hữu kết cấu thạch mọng nước, kết hợp nước cất hoa hồng hữu cơ, Pentavitin, axit amin và Hyaluronic Acid (HA), giúp cấp ẩm, duy trì độ ẩm và hỗ trợ nuôi dưỡng làn da mềm mại, mịn màng. Công thức giúp bổ sung lượng nước cần thiết, hạn chế tình trạng da khô ráp, đồng thời hỗ trợ củng cố hàng rào bảo vệ tự nhiên của da. Nhờ khả năng giữ ẩm, sản phẩm giúp làn da trông căng mịn, tươi tắn và đầy sức sống hơn. Kết cấu thạch tạo cảm giác ẩm mát, phù hợp để sử dụng trong chu trình chăm sóc da hằng ngày.",
        "variants": [
            {
                "size": 30.0,
                "unit": "ml",
                "price": 172000
            },
            {
                "size": 100.0,
                "unit": "ml",
                "price": 320000
            }
        ],
        "brand_code": "H6",
        "type_code": "L3"
    },
    {
        "id": "S27",
        "name": "Kem dưỡng ẩm, làm dịu da tức thì Hada Labo Advanced Nourish Cream",
        "type": "Kem dưỡng",
        "brand": "Hada Labo",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da hỗn hợp",
            "Da nhạy cảm"
        ],
        "description": "Kem dưỡng ẩm Hada Labo Advanced Nourish được thiết kế dành cho làn da khô ráp, thiếu ẩm và nhạy cảm, giúp cấp nước, duy trì độ ẩm và hỗ trợ cải thiện hàng rào bảo vệ tự nhiên của da. Sản phẩm nổi bật với hệ dưỡng 5 loại Hyaluronic Acid (HA), giúp bổ sung độ ẩm ở nhiều cấp độ, hạn chế tình trạng mất nước và mang lại làn da mềm mại, căng mịn. Công thức còn hỗ trợ làm dịu những vùng da khô, cải thiện độ đàn hồi và giúp da trông khỏe mạnh, tươi tắn hơn. Với kết cấu kem mỏng nhẹ, thấm nhanh và không gây cảm giác nhờn rít, sản phẩm phù hợp để sử dụng hằng ngày vào buổi sáng và tối, giúp duy trì làn da ẩm mượt và dễ chịu.",
        "variants": [
            {
                "size": 50.0,
                "unit": "g",
                "price": 195000
            }
        ],
        "brand_code": "H10",
        "type_code": "L3"
    },
    {
        "id": "S28",
        "name": "Kem Dưỡng Ẩm Phục Hồi Embryolisse Lait Creme Concentre",
        "type": "Kem dưỡng",
        "brand": "Embryolisse",
        "skin_types": [
            "Da thường",
            "Da khô"
        ],
        "description": "Kem dưỡng ẩm phục hồi Lait-Crème Concentré là sản phẩm chăm sóc da đa năng đến từ Pháp, nổi bật với công thức kết hợp các thành phần dưỡng ẩm và làm mềm da. Sản phẩm chứa nha đam hữu cơ, bơ hạt mỡ, sáp ong và protein đậu nành, giúp bổ sung độ ẩm, duy trì màng ẩm tự nhiên và hỗ trợ củng cố hàng rào bảo vệ da. Công thức giúp làm dịu cảm giác khô căng, cải thiện tình trạng da thô ráp, mang lại làn da mềm mại, mịn màng và tươi tắn hơn. Với khả năng dưỡng ẩm và làm mềm da, sản phẩm có thể được sử dụng trong chu trình chăm sóc da hằng ngày, đồng thời hỗ trợ tạo lớp nền ẩm mượt trước khi trang điểm.",
        "variants": [
            {
                "size": 5.0,
                "unit": "ml",
                "price": 149000
            },
            {
                "size": 15.0,
                "unit": "ml",
                "price": 250000
            },
            {
                "size": 30.0,
                "unit": "ml",
                "price": 335000
            },
            {
                "size": 75.0,
                "unit": "ml",
                "price": 578000
            }
        ],
        "brand_code": "H17",
        "type_code": "L3"
    },
    {
        "id": "S29",
        "name": "Kem dưỡng ẩm Garnier Water Gel",
        "type": "Kem dưỡng",
        "brand": "Garnier",
        "skin_types": [
            "Da thường",
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Kem dưỡng ẩm Water Gel là sản phẩm chăm sóc da có kết cấu dạng gel mỏng nhẹ, giúp cấp nước, duy trì độ ẩm và hỗ trợ cải thiện vẻ ngoài tươi sáng của làn da. Sản phẩm kết hợp Hyaluronic Acid (HA), Niacinamide và Vitamin C nhằm đáp ứng nhu cầu dưỡng ẩm, làm dịu và chăm sóc da hằng ngày. HA giúp giữ nước, mang lại làn da mềm mại, căng mịn; Niacinamide hỗ trợ củng cố hàng rào bảo vệ da, cải thiện tình trạng da không đều màu và làm mờ sự xuất hiện của vết thâm; Vitamin C góp phần cải thiện độ rạng rỡ và hỗ trợ làm sáng da. Với kết cấu Water Gel dễ tán, thấm nhanh và ít gây cảm giác nhờn rít, sản phẩm phù hợp với điều kiện khí hậu nóng ẩm, giúp da duy trì độ ẩm mà không tạo cảm giác nặng mặt.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 178000
            }
        ],
        "brand_code": "H2",
        "type_code": "L3"
    },
    {
        "id": "S30",
        "name": "Kem Dưỡng Ẩm Hatomugi",
        "type": "Kem dưỡng",
        "brand": "Reihaku",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da hỗn hợp"
        ],
        "description": "Kem dưỡng ẩm và làm sáng da Reihaku Hatomugi Milky Cream là kem dưỡng ẩm – làm sáng – mờ thâm từ xứ sở Nhật Bản. Giúp cải thiện độ đàn hồi của da, cho da mềm mịn, chống thô ráp. Làm sáng da, làm dịu viêm mụn, cải thiện thâm mụn. Cho cảm giác tươi mát, nhẹ nhàng, thoải mái ngay khi chạm vào da. Giữ cho lớp trang điểm lâu bền hơn. Thành phần chính chiết xuất hạt Ý dĩ kết hợp với Hyaluronic Acid giúp tăng cường độ ẩm cho da mềm mại, mịn màng. Đồng thời làm sáng da và giảm thiểu những tác hại từ môi trường khiến da bị lão hóa.",
        "variants": [
            {
                "size": 300.0,
                "unit": "g",
                "price": 145000
            }
        ],
        "brand_code": "H18",
        "type_code": "L3"
    },
    {
        "id": "S31",
        "name": "Kem chống nắng BEPLAIN Sunmuse",
        "type": "Kem chống nắng",
        "brand": "Beplain",
        "skin_types": [
            "Da thường",
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Kem chống nắng BEPLAIN Sunmuse là sản phẩm chống nắng hóa học kết hợp dưỡng ẩm, giúp bảo vệ làn da trước tác động của tia UVA và UVB với chỉ số SPF 50+ PA++++. Sản phẩm hỗ trợ hạn chế những ảnh hưởng tiêu cực của ánh nắng mặt trời, góp phần ngăn ngừa tình trạng da sạm màu và lão hóa sớm do tia UV. Bên cạnh khả năng chống nắng, sản phẩm còn chú trọng đến việc duy trì độ ẩm tự nhiên, giúp da mềm mại, hạn chế cảm giác khô căng và hỗ trợ củng cố hàng rào bảo vệ da. Với kết cấu dạng kem, sản phẩm có thể được sử dụng trong chu trình chăm sóc da hằng ngày, đặc biệt vào buổi sáng trước khi tiếp xúc với môi trường bên ngoài. Khi sử dụng đều đặn và đúng cách, kem chống nắng góp phần bảo vệ làn da, duy trì vẻ ngoài tươi tắn và hỗ trợ chăm sóc da lâu dài.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 340000
            }
        ],
        "brand_code": "H16",
        "type_code": "L4"
    },
    {
        "id": "S32",
        "name": "Sữa chống nắng L’Oréal Paris",
        "type": "Kem chống nắng",
        "brand": "L’Oréal Paris",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Sữa chống nắng UV Defender Invisible Resist SPF 50+ PA++++ là sản phẩm chống nắng phổ rộng giúp bảo vệ làn da trước tác động của tia UVA và UVB. Sản phẩm kết hợp các màng lọc chống nắng Mexoryl SX và Mexoryl XL cùng công nghệ Netlock, giúp hình thành lớp màng bảo vệ đồng đều trên bề mặt da, hỗ trợ duy trì hiệu quả chống nắng trong quá trình hoạt động hằng ngày. Với kết cấu dạng sữa mỏng nhẹ, sản phẩm dễ tán, tạo lớp phủ gần như vô hình và hạn chế cảm giác nặng mặt. Công thức được thiết kế nhằm tăng khả năng chống chịu trước các tác động từ môi trường như nước, mồ hôi, nhiệt độ, ma sát, cát và ô nhiễm. Sản phẩm phù hợp để sử dụng hằng ngày, đặc biệt khi tham gia các hoạt động ngoài trời.",
        "variants": [
            {
                "size": 100.0,
                "unit": "ml",
                "price": 294000
            }
        ],
        "brand_code": "H?",
        "type_code": "L4"
    },
    {
        "id": "S33",
        "name": "Kem Chống Nắng Make P:rem",
        "type": "Kem chống nắng",
        "brand": "Make P:rem",
        "skin_types": [
            "Da hỗn hợp",
            "Da thường",
            "Da nhạy cảm"
        ],
        "description": "Make P:rem là thương hiệu mỹ phẩm đến từ Hàn Quốc, nổi bật với các sản phẩm chăm sóc da chú trọng tính an toàn, hiệu quả và sự tối giản trong quy trình dưỡng da. Thương hiệu kết hợp các thành phần chăm sóc da được lựa chọn kỹ lưỡng với công nghệ mỹ phẩm hiện đại nhằm đáp ứng nhiều nhu cầu khác nhau như làm sạch, cấp ẩm, làm dịu và bảo vệ da. Danh mục sản phẩm của Make P:rem đa dạng, bao gồm sữa rửa mặt, toner, serum, kem dưỡng ẩm và kem chống nắng. Các sản phẩm hướng đến việc duy trì độ ẩm, hỗ trợ củng cố hàng rào bảo vệ da và giúp làn da khỏe mạnh trước những tác động từ môi trường. Với định hướng phát triển các giải pháp chăm sóc da thiết thực, Make P:rem là lựa chọn đáng cân nhắc cho những người muốn xây dựng chu trình dưỡng da đơn giản và phù hợp với nhu cầu cá nhân.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 379000
            }
        ],
        "brand_code": "H19",
        "type_code": "L4"
    },
    {
        "id": "S34",
        "name": "Kem chống nắng Dermablock",
        "type": "Kem chống nắng",
        "brand": "Dermablock",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da hỗn hợp",
            "Da nhạy cảm"
        ],
        "description": "Dermablock là dòng sản phẩm chống nắng thuộc thương hiệu Cell Fusion C đến từ Hàn Quốc, kế thừa nền tảng nghiên cứu và công nghệ chăm sóc da của thương hiệu với hơn 20 năm kinh nghiệm. Dermablock được phát triển với sứ mệnh bảo vệ làn da trước những tác động có hại từ môi trường, đặc biệt là tia UVA và UVB từ ánh nắng mặt trời. Các sản phẩm chú trọng khả năng chống nắng kết hợp chăm sóc da, góp phần duy trì độ ẩm và hỗ trợ bảo vệ hàng rào tự nhiên của da. Với định hướng ứng dụng công nghệ tiên tiến vào các giải pháp chống nắng, Dermablock mang đến những lựa chọn phù hợp cho nhu cầu bảo vệ da hằng ngày, giúp người dùng chủ động chăm sóc và duy trì làn da khỏe mạnh.",
        "variants": [
            {
                "size": 35.0,
                "unit": "ml",
                "price": 218000
            }
        ],
        "brand_code": "H20",
        "type_code": "L4"
    },
    {
        "id": "S35",
        "name": "Kem chống nắng Sunplay Skin Aqua Clear White",
        "type": "Kem chống nắng",
        "brand": "Sunplay",
        "skin_types": [
            "Da thường",
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Sữa chống nắng Sunplay Skin Aqua Clear White SPF 50+ PA++++ là sản phẩm chống nắng hằng ngày được thiết kế dành cho làn da dầu, giúp bảo vệ da trước tác động của tia UVA, UVB và các yếu tố môi trường. Sản phẩm ứng dụng công nghệ chống nắng phổ rộng, kết hợp các thành phần dưỡng da như Vitamin C, Vitamin B3 (Niacinamide) và Ceramide, vừa hỗ trợ bảo vệ da vừa cải thiện vẻ ngoài sáng mịn, đồng thời duy trì độ ẩm tự nhiên. Với kết cấu dạng sữa mỏng nhẹ, sản phẩm thấm nhanh, tạo cảm giác thông thoáng và hạn chế bóng nhờn trong quá trình sử dụng. Khả năng kháng nước và mồ hôi giúp sản phẩm phù hợp với các hoạt động hằng ngày, kể cả khi thời tiết nóng ẩm. Sản phẩm thuộc dòng Eco Vietnam, hướng đến việc phát triển các giải pháp chăm sóc da gắn với ý thức bảo vệ môi trường.",
        "variants": [
            {
                "size": 25.0,
                "unit": "ml",
                "price": 199000
            }
        ],
        "brand_code": "H21",
        "type_code": "L4"
    },
    {
        "id": "S36",
        "name": "Kem Chống Nắng La Roche Posay Anthelios Anti-Shine Dry Touch Gel Cream",
        "type": "Kem chống nắng",
        "brand": "La Roche Posay",
        "skin_types": [
            "Da dầu",
            "Da hỗn hợp",
            "Da nhạy cảm",
            "Da mụn"
        ],
        "description": "Kem chống nắng La Roche-Posay Anthelios Anti-Shine Dry Touch Gel-Cream SPF 50++ là sản phẩm chống nắng được thiết kế dành cho làn da có xu hướng tiết nhiều dầu, giúp bảo vệ da trước tác động của tia UVA và UVB. Sản phẩm nổi bật với kết cấu dạng gel-cream, mang lại cảm giác khô thoáng sau khi thoa, hỗ trợ kiểm soát bóng nhờn và hạn chế tình trạng da bóng dầu trong ngày. Bên cạnh khả năng chống nắng, sản phẩm còn giúp bảo vệ làn da trước những tác động từ môi trường, góp phần hạn chế tình trạng sạm da và lão hóa sớm do ánh nắng mặt trời. Với đặc tính thấm nhanh và bề mặt ráo mịn, kem chống nắng có thể sử dụng hằng ngày và kết hợp với các bước trang điểm, phù hợp với người yêu thích lớp nền nhẹ, ít bóng nhờn.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 357000
            }
        ],
        "brand_code": "H5",
        "type_code": "L4"
    },
    {
        "id": "S37",
        "name": "Kem Chống Nắng Caryophy",
        "type": "Kem chống nắng",
        "brand": "Caryophy",
        "skin_types": [
            "Da dầu",
            "Da hỗn hợp",
            "Da nhạy cảm",
            "Da mụn"
        ],
        "description": "Kem chống nắng Caryophy có các thành phần nổi bật như Zinc Oxide, Titanium Dioxide và Ethylhexyl Methoxycinnamate giúp bảo vệ da trước tác động của tia UV. Sản phẩm còn chứa Repair Complex CLR (Bifida Ferment Lysate), Vitamin F Forte CLR, MultiMoist CLR, chiết xuất rau sam, rau má và nho, góp phần dưỡng ẩm, làm dịu và hỗ trợ phục hồi hàng rào bảo vệ da. Bên cạnh đó, Hydrogenated Phosphatidylcholine và Caprylic/Capric Triglyceride giúp dưỡng da mềm mại hơn.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 376000
            }
        ],
        "brand_code": "H15",
        "type_code": "L4"
    },
    {
        "id": "S38",
        "name": "Kem chống nắng nâng tone Tím d'Alba White Truffle Tone Up Sunscreen (Purple)",
        "type": "Kem chống nắng",
        "brand": "d’ Alba",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Kem chống nắng d’Alba có xuất xứ từ Hàn Quốc, nổi bật với các thành phần chống nắng như Titanium Dioxide, Diethylaminohydroxybenzoylhexyl Benzoate và Ethylhexyl Triazone, giúp bảo vệ da trước tác động của tia UV. Sản phẩm còn chứa Niacinamide hỗ trợ làm sáng da, kết hợp với chiết xuất rau má, rau sam, lá ô liu, cùng các thành phần dưỡng da như Glycerin, Squalane, Panthenol, Allantoin và Hyaluronic Acid giúp dưỡng ẩm, làm dịu và duy trì độ mềm mại cho da. Sản phẩm có thể mang lại hiệu ứng nâng tông, giúp làn da trông tươi sáng và đều màu hơn. Kem chống nắng d’Alba được giới thiệu phù hợp với mọi loại da, kể cả da nhạy cảm, tuy nhiên khả năng dung nạp còn tùy thuộc vào từng cá nhân.",
        "variants": [
            {
                "size": 50.0,
                "unit": "ml",
                "price": 379000
            }
        ],
        "brand_code": "H22",
        "type_code": "L4"
    },
    {
        "id": "S39",
        "name": "Sữa Chống Nắng Vô Cơ Sen Hậu Giang",
        "type": "Kem chống nắng",
        "brand": "Cocoon",
        "skin_types": [
            "Da nhạy cảm"
        ],
        "description": "Sữa chống nắng vô cơ Cocoon chiết xuất sen Hậu Giang, sử dụng màng lọc khoáng chất Zinc Oxide và Titanium Dioxide giúp bảo vệ da phổ rộng trước tia UVA/UVB. Công thức thuần chay, không chứa cồn khô, paraben và dầu khoáng. Kết cấu nâng tông Beige tự nhiên, hỗ trợ chống oxy hóa, kiềm dầu và tạo lớp nền nhẹ nhàng. Phù hợp với nhiều loại da, đặc biệt là da nhạy cảm và người yêu thích lớp chống nắng nâng tông tự nhiên.",
        "variants": [
            {
                "size": 15.0,
                "unit": "ml",
                "price": 195000
            },
            {
                "size": 50.0,
                "unit": "ml",
                "price": 295000
            }
        ],
        "brand_code": "H6",
        "type_code": "L4"
    },
    {
        "id": "S40",
        "name": "Kem chống nắng nâng tông da Dive-In",
        "type": "Kem chống nắng",
        "brand": "Torriden",
        "skin_types": [
            "Da thường",
            "Da khô",
            "Da dầu",
            "Da hỗn hợp"
        ],
        "description": "Kem chống nắng DIVE IN Tone Up Sun Cream Purple SPF 50+ PA++++ có kết cấu mỏng nhẹ, mềm mịn như lụa, giúp bảo vệ da trước tác động của tia UV, đồng thời nâng tông và hỗ trợ làm đều màu da. Công thức màu tím giúp trung hòa sắc vàng, cải thiện vẻ ngoài của làn da xỉn màu, mang lại lớp nền sáng mịn và tự nhiên. Sản phẩm chứa 10D Hyaluronic Acid giúp duy trì độ ẩm, mang lại cảm giác mềm mại, hạn chế tình trạng khô da và bết dính. Kem có hiệu ứng nâng tông lâu trôi, giúp bề mặt da trông mịn màng hơn và có thể sử dụng thay kem lót trước khi trang điểm. Sản phẩm phù hợp với làn da cần chống nắng, đặc biệt là da có sắc vàng hoặc màu da không đều.",
        "variants": [
            {
                "size": 60.0,
                "unit": "ml",
                "price": 325000
            }
        ],
        "brand_code": "H13",
        "type_code": "L4"
    }
]

TYPE_CODES = {
    "Nước tẩy trang": "L1",
    "Sữa rửa mặt": "L2",
    "Kem dưỡng": "L3",
    "Kem chống nắng": "L4",
}
BRAND_CODES = {
    "Bioderma": "H1", "Garnier": "H2", "L'Oréal Paris": "H3",
    "Simple": "H4", "La Roche-Posay": "H5", "La Roche Posay": "H5",
    "Cocoon": "H6", "Dr.Ceutics": "H7", "Cetaphil": "H8",
    "CeraVe": "H9", "Hada Labo": "H10", "SVR": "H11",
    "Eucerin": "H12", "Torriden": "H13", "Neutrogena": "H14",
    "Caryophy": "H15", "Beplain": "H16", "Embryolisse": "H17",
    "Reihaku": "H18", "Make P:rem": "H19", "Dermablock": "H20",
    "Sunplay": "H21", "d’ Alba": "H22", "d'Alba": "H22",
}
SKIN_CODES = {
    "Da thường": "D1",
    "Da khô": "D2",
    "Da dầu": "D3",
    "Da hỗn hợp": "D4",
    "Da nhạy cảm": "D5",
    "Da đang điều trị": "D6",
    "Da mụn": "D7",
}

def get_size_code(size, unit):
    """Mã hóa dung tích theo bảng mã trong báo cáo."""
    if size is None:
        return "T?"
    if unit == "g":
        if size < 100:
            return "T9"
        if size < 200:
            return "T10"
        if size < 300:
            return "T11"
        return "T12"
    if size < 20:
        return "T1"
    if size < 50:
        return "T2"
    if size < 100:
        return "T3"
    if size < 200:
        return "T4"
    if size < 300:
        return "T5"
    if size < 500:
        return "T6"
    if size < 1000:
        return "T7"
    return "T8"

def get_price_code(price):
    """G1: dưới 100k; G2: 100k-<200k; G3: 200k-<400k; G4: từ 400k."""
    if price < 100_000:
        return "G1"
    if price < 200_000:
        return "G2"
    if price < 400_000:
        return "G3"
    return "G4"

def format_money(value):
    return f"{value:,.0f}".replace(",", ".") + "đ"

def format_size(variant):
    if variant["size"] is None:
        return "Chưa rõ dung tích"
    size = variant["size"]
    shown = str(int(size)) if float(size).is_integer() else str(size)
    return f"{shown} {variant['unit']}"

def infer_products(skin_type, product_type, brand, size_group, price_group):
    """
    BỘ SUY DIỄN:
    kiểm tra từng sản phẩm và từng biến thể dung tích/giá theo các sự kiện
    người dùng đã chọn. Trả về sản phẩm phù hợp cùng luật đã kích hoạt.
    """
    results = []

    for product in PRODUCTS:
        if product_type != "Tất cả" and product["type"] != product_type:
            continue
        if brand != "Tất cả" and product["brand"] != brand:
            # Một số tên thương hiệu trong báo cáo có cách viết khác nhau.
            if not (brand == "La Roche-Posay" and product["brand"] == "La Roche Posay"):
                if not (brand == "d'Alba" and product["brand"] == "d’ Alba"):
                    continue
        if skin_type != "Tất cả" and skin_type not in product["skin_types"]:
            continue

        matched_variants = []
        for variant in product["variants"]:
            scode = get_size_code(variant["size"], variant["unit"])
            gcode = get_price_code(variant["price"])

            # Dung tích được lọc theo mã nhóm T1–T12 trong báo cáo NHÓM 13.
            if size_group != "Tất cả" and scode != size_group:
                continue
            if price_group != "Tất cả" and gcode != price_group:
                continue
            matched_variants.append(variant)

        if not matched_variants:
            continue

        # Tạo luật giải thích. Khi người dùng bỏ qua một tiêu chí,
        # hệ thống dùng giá trị cụ thể của biến thể/sản phẩm để hiển thị luật.
        variant = matched_variants[0]
        lcode = TYPE_CODES.get(product["type"], "L?")
        hcode = BRAND_CODES.get(product["brand"], "H?")
        dcode = SKIN_CODES.get(skin_type, "") if skin_type != "Tất cả" else (
            SKIN_CODES.get(product["skin_types"][0], "D?") if product["skin_types"] else "D?"
        )
        tcode = get_size_code(variant["size"], variant["unit"])
        gcode = get_price_code(variant["price"])
        # Ưu tiên luật có sẵn trong báo cáo; nếu tổ hợp không được liệt kê
        # trong tập luật gốc thì tạo luật giải thích từ dữ liệu sản phẩm.
        report_rule = next(
            (
                item["expression"] for item in RULES
                if item["product_id"] == product["id"]
                and item["type_code"] == lcode
                and item["brand_code"] == hcode
                and item["skin_code"] == dcode
                and item["size_code"] == tcode
                and item["price_code"] == gcode
            ),
            None,
        )
        rule = report_rule or (
            f"{lcode} ∧ {hcode} ∧ {dcode} ∧ {tcode} ∧ {gcode} → {product['id']}"
        )

        results.append({
            "product": product,
            "variants": matched_variants,
            "rule": rule,
        })

    return results

# ==========================================================
# 2. GIAO DIỆN NGƯỜI DÙNG
# Các bộ lọc phụ thuộc vào những sản phẩm thực sự có trong dữ liệu.
# ==========================================================
SIZE_LABELS = {
    "T1": "Dưới 20 ml",
    "T2": "Từ 20 ml đến dưới 50 ml",
    "T3": "Từ 50 ml đến dưới 100 ml",
    "T4": "Từ 100 ml đến dưới 200 ml",
    "T5": "Từ 200 ml đến dưới 300 ml",
    "T6": "Từ 300 ml đến dưới 500 ml",
    "T7": "Từ 500 ml đến dưới 1.000 ml",
    "T8": "Từ 1.000 ml trở lên",
    "T9": "Dưới 100 g",
    "T10": "Từ 100 g đến dưới 200 g",
    "T11": "Từ 200 g đến dưới 300 g",
    "T12": "Từ 300 g trở lên",
}

PRICE_LABELS = {
    "G1": "Dưới 100.000đ",
    "G2": "Từ 100.000đ đến dưới 200.000đ",
    "G3": "Từ 200.000đ đến dưới 400.000đ",
    "G4": "Từ 400.000đ trở lên",
}


# TẬP LUẬT CHÍNH THỨC trích từ mục 2.2 trong báo cáo NHÓM 13.docx.
# Giữ nguyên các tổ hợp mã điều kiện và mã sản phẩm của báo cáo.
RULES = [{'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D2', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S1', 'expression': 'L1 ∧ H1 ∧ D2 ∧ T4 ∧ G2 → S1'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D2', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S1', 'expression': 'L1 ∧ H1 ∧ D2 ∧ T5 ∧ G3 → S1'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D2', 'size_code': 'T7', 'price_code': 'G4', 'product_id': 'S1', 'expression': 'L1 ∧ H1 ∧ D2 ∧ T7 ∧ G4 → S1'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D5', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S1', 'expression': 'L1 ∧ H1 ∧ D5 ∧ T4 ∧ G2 → S1'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D5', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S1', 'expression': 'L1 ∧ H1 ∧ D5 ∧ T5 ∧ G3 → S1'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D5', 'size_code': 'T7', 'price_code': 'G4', 'product_id': 'S1', 'expression': 'L1 ∧ H1 ∧ D5 ∧ T7 ∧ G4 → S1'}, {'type_code': 'L1', 'brand_code': 'H2', 'skin_code': 'D1', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S2', 'expression': 'L1 ∧ H2 ∧ D1 ∧ T6 ∧ G2 → S2'}, {'type_code': 'L1', 'brand_code': 'H2', 'skin_code': 'D1', 'size_code': 'T7', 'price_code': 'G2', 'product_id': 'S2', 'expression': 'L1 ∧ H2 ∧ D1 ∧ T7 ∧ G2 → S2'}, {'type_code': 'L1', 'brand_code': 'H2', 'skin_code': 'D5', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S2', 'expression': 'L1 ∧ H2 ∧ D5 ∧ T6 ∧ G2 → S2'}, {'type_code': 'L1', 'brand_code': 'H2', 'skin_code': 'D5', 'size_code': 'T7', 'price_code': 'G2', 'product_id': 'S2', 'expression': 'L1 ∧ H2 ∧ D5 ∧ T7 ∧ G2 → S2'}, {'type_code': 'L1', 'brand_code': 'H3', 'skin_code': 'D3', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S3', 'expression': 'L1 ∧ H3 ∧ D3 ∧ T6 ∧ G2 → S3'}, {'type_code': 'L1', 'brand_code': 'H3', 'skin_code': 'D4', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S3', 'expression': 'L1 ∧ H3 ∧ D4 ∧ T6 ∧ G2 → S3'}, {'type_code': 'L1', 'brand_code': 'H3', 'skin_code': 'D6', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S3', 'expression': 'L1 ∧ H3 ∧ D6 ∧ T6 ∧ G2 → S3'}, {'type_code': 'L1', 'brand_code': 'H4', 'skin_code': 'D1', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S4', 'expression': 'L1 ∧ H4 ∧ D1 ∧ T6 ∧ G2 → S4'}, {'type_code': 'L1', 'brand_code': 'H4', 'skin_code': 'D2', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S4', 'expression': 'L1 ∧ H4 ∧ D2 ∧ T6 ∧ G2 → S4'}, {'type_code': 'L1', 'brand_code': 'H4', 'skin_code': 'D3', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S4', 'expression': 'L1 ∧ H4 ∧ D3 ∧ T6 ∧ G2 → S4'}, {'type_code': 'L1', 'brand_code': 'H4', 'skin_code': 'D5', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S4', 'expression': 'L1 ∧ H4 ∧ D5 ∧ T6 ∧ G2 → S4'}, {'type_code': 'L1', 'brand_code': 'H5', 'skin_code': 'D5', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S5', 'expression': 'L1 ∧ H5 ∧ D5 ∧ T5 ∧ G3 → S5'}, {'type_code': 'L1', 'brand_code': 'H5', 'skin_code': 'D5', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S5', 'expression': 'L1 ∧ H5 ∧ D5 ∧ T6 ∧ G3 → S5'}, {'type_code': 'L1', 'brand_code': 'H2', 'skin_code': 'D2', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S6', 'expression': 'L1 ∧ H2 ∧ D2 ∧ T6 ∧ G2 → S6'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D3', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D3 ∧ T4 ∧ G2 → S7'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D3', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D3 ∧ T5 ∧ G3 → S7'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D3', 'size_code': 'T7', 'price_code': 'G4', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D3 ∧ T7 ∧ G4 → S7'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D4', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D4 ∧ T4 ∧ G2 → S7'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D4', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D4 ∧ T5 ∧ G3 → S7'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D4', 'size_code': 'T7', 'price_code': 'G4', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D4 ∧ T7 ∧ G4 → S7'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D7', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D7 ∧ T4 ∧ G2 → S7'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D7', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D7 ∧ T5 ∧ G3 → S7'}, {'type_code': 'L1', 'brand_code': 'H1', 'skin_code': 'D7', 'size_code': 'T7', 'price_code': 'G4', 'product_id': 'S7', 'expression': 'L1 ∧ H1 ∧ D7 ∧ T7 ∧ G4 → S7'}, {'type_code': 'L1', 'brand_code': 'H3', 'skin_code': 'D1', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S8', 'expression': 'L1 ∧ H3 ∧ D1 ∧ T6 ∧ G2 → S8'}, {'type_code': 'L1', 'brand_code': 'H3', 'skin_code': 'D2', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S8', 'expression': 'L1 ∧ H3 ∧ D2 ∧ T6 ∧ G2 → S8'}, {'type_code': 'L1', 'brand_code': 'H3', 'skin_code': 'D6', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S8', 'expression': 'L1 ∧ H3 ∧ D6 ∧ T6 ∧ G2 → S8'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D3', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D3 ∧ T4 ∧ G2 → S9'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D3', 'size_code': 'T7', 'price_code': 'G3', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D3 ∧ T7 ∧ G3 → S9'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D3', 'size_code': 'T8', 'price_code': 'G3', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D3 ∧ T8 ∧ G3 → S9'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D4', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D4 ∧ T4 ∧ G2 → S9'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D4', 'size_code': 'T7', 'price_code': 'G3', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D4 ∧ T7 ∧ G3 → S9'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D4', 'size_code': 'T8', 'price_code': 'G3', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D4 ∧ T8 ∧ G3 → S9'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D7', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D7 ∧ T4 ∧ G2 → S9'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D7', 'size_code': 'T7', 'price_code': 'G3', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D7 ∧ T7 ∧ G3 → S9'}, {'type_code': 'L1', 'brand_code': 'H6', 'skin_code': 'D7', 'size_code': 'T8', 'price_code': 'G3', 'product_id': 'S9', 'expression': 'L1 ∧ H6 ∧ D7 ∧ T8 ∧ G3 → S9'}, {'type_code': 'L1', 'brand_code': 'H7', 'skin_code': 'D2', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S10', 'expression': 'L1 ∧ H7 ∧ D2 ∧ T6 ∧ G2 → S10'}, {'type_code': 'L1', 'brand_code': 'H7', 'skin_code': 'D2', 'size_code': 'T7', 'price_code': 'G2', 'product_id': 'S10', 'expression': 'L1 ∧ H7 ∧ D2 ∧ T7 ∧ G2 → S10'}, {'type_code': 'L1', 'brand_code': 'H7', 'skin_code': 'D3', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S10', 'expression': 'L1 ∧ H7 ∧ D3 ∧ T6 ∧ G2 → S10'}, {'type_code': 'L1', 'brand_code': 'H7', 'skin_code': 'D3', 'size_code': 'T7', 'price_code': 'G2', 'product_id': 'S10', 'expression': 'L1 ∧ H7 ∧ D3 ∧ T7 ∧ G2 → S10'}, {'type_code': 'L1', 'brand_code': 'H7', 'skin_code': 'D4', 'size_code': 'T6', 'price_code': 'G2', 'product_id': 'S10', 'expression': 'L1 ∧ H7 ∧ D4 ∧ T6 ∧ G2 → S10'}, {'type_code': 'L1', 'brand_code': 'H7', 'skin_code': 'D4', 'size_code': 'T7', 'price_code': 'G2', 'product_id': 'S10', 'expression': 'L1 ∧ H7 ∧ D4 ∧ T7 ∧ G2 → S10'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D5', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D5 ∧ T4 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D5', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D5 ∧ T5 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D5', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D5 ∧ T6 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D5', 'size_code': 'T8', 'price_code': 'G4', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D5 ∧ T8 ∧ G4 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D6', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D6 ∧ T4 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D6', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D6 ∧ T5 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D6', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D6 ∧ T6 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D6', 'size_code': 'T8', 'price_code': 'G4', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D6 ∧ T8 ∧ G4 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D7', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D7 ∧ T4 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D7', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D7 ∧ T5 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D7', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D7 ∧ T6 ∧ G3 → S11'}, {'type_code': 'L2', 'brand_code': 'H8', 'skin_code': 'D7', 'size_code': 'T8', 'price_code': 'G4', 'product_id': 'S11', 'expression': 'L2 ∧ H8 ∧ D7 ∧ T8 ∧ G4 → S11'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S12', 'expression': 'L2 ∧ H9 ∧ D1 ∧ T3 ∧ G2 → S12'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D1', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S12', 'expression': 'L2 ∧ H9 ∧ D1 ∧ T5 ∧ G3 → S12'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D1', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S12', 'expression': 'L2 ∧ H9 ∧ D1 ∧ T6 ∧ G3 → S12'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S12', 'expression': 'L2 ∧ H9 ∧ D3 ∧ T3 ∧ G2 → S12'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D3', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S12', 'expression': 'L2 ∧ H9 ∧ D3 ∧ T5 ∧ G3 → S12'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D3', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S12', 'expression': 'L2 ∧ H9 ∧ D3 ∧ T6 ∧ G3 → S12'}, {'type_code': 'L2', 'brand_code': 'H5', 'skin_code': 'D3', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S13', 'expression': 'L2 ∧ H5 ∧ D3 ∧ T5 ∧ G3 → S13'}, {'type_code': 'L2', 'brand_code': 'H5', 'skin_code': 'D3', 'size_code': 'T6', 'price_code': 'G4', 'product_id': 'S13', 'expression': 'L2 ∧ H5 ∧ D3 ∧ T6 ∧ G4 → S13'}, {'type_code': 'L2', 'brand_code': 'H5', 'skin_code': 'D5', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S13', 'expression': 'L2 ∧ H5 ∧ D5 ∧ T5 ∧ G3 → S13'}, {'type_code': 'L2', 'brand_code': 'H5', 'skin_code': 'D5', 'size_code': 'T6', 'price_code': 'G4', 'product_id': 'S13', 'expression': 'L2 ∧ H5 ∧ D5 ∧ T6 ∧ G4 → S13'}, {'type_code': 'L2', 'brand_code': 'H4', 'skin_code': 'D5', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S14', 'expression': 'L2 ∧ H4 ∧ D5 ∧ T4 ∧ G2 → S14'}, {'type_code': 'L2', 'brand_code': 'H10', 'skin_code': 'D1', 'size_code': 'T9', 'price_code': 'G1', 'product_id': 'S15', 'expression': 'L2 ∧ H10 ∧ D1 ∧ T9 ∧ G1 → S15'}, {'type_code': 'L2', 'brand_code': 'H10', 'skin_code': 'D2', 'size_code': 'T9', 'price_code': 'G1', 'product_id': 'S15', 'expression': 'L2 ∧ H10 ∧ D2 ∧ T9 ∧ G1 → S15'}, {'type_code': 'L2', 'brand_code': 'H10', 'skin_code': 'D3', 'size_code': 'T9', 'price_code': 'G1', 'product_id': 'S15', 'expression': 'L2 ∧ H10 ∧ D3 ∧ T9 ∧ G1 → S15'}, {'type_code': 'L2', 'brand_code': 'H10', 'skin_code': 'D4', 'size_code': 'T9', 'price_code': 'G1', 'product_id': 'S15', 'expression': 'L2 ∧ H10 ∧ D4 ∧ T9 ∧ G1 → S15'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S16', 'expression': 'L2 ∧ H9 ∧ D1 ∧ T3 ∧ G2 → S16'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D1', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S16', 'expression': 'L2 ∧ H9 ∧ D1 ∧ T5 ∧ G3 → S16'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D1', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S16', 'expression': 'L2 ∧ H9 ∧ D1 ∧ T6 ∧ G3 → S16'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D2', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S16', 'expression': 'L2 ∧ H9 ∧ D2 ∧ T3 ∧ G2 → S16'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D2', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S16', 'expression': 'L2 ∧ H9 ∧ D2 ∧ T5 ∧ G3 → S16'}, {'type_code': 'L2', 'brand_code': 'H9', 'skin_code': 'D2', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S16', 'expression': 'L2 ∧ H9 ∧ D2 ∧ T6 ∧ G3 → S16'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D3 ∧ T3 ∧ G2 → S17'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D3', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D3 ∧ T5 ∧ G3 → S17'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D3', 'size_code': 'T6', 'price_code': 'G4', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D3 ∧ T6 ∧ G4 → S17'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D5', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D5 ∧ T3 ∧ G2 → S17'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D5', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D5 ∧ T5 ∧ G3 → S17'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D5', 'size_code': 'T6', 'price_code': 'G4', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D5 ∧ T6 ∧ G4 → S17'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D7', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D7 ∧ T3 ∧ G2 → S17'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D7', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D7 ∧ T5 ∧ G3 → S17'}, {'type_code': 'L2', 'brand_code': 'H11', 'skin_code': 'D7', 'size_code': 'T6', 'price_code': 'G4', 'product_id': 'S17', 'expression': 'L2 ∧ H11 ∧ D7 ∧ T6 ∧ G4 → S17'}, {'type_code': 'L2', 'brand_code': 'H1', 'skin_code': 'D3', 'size_code': 'T2', 'price_code': 'G2', 'product_id': 'S18', 'expression': 'L2 ∧ H1 ∧ D3 ∧ T2 ∧ G2 → S18'}, {'type_code': 'L2', 'brand_code': 'H1', 'skin_code': 'D3', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S18', 'expression': 'L2 ∧ H1 ∧ D3 ∧ T5 ∧ G3 → S18'}, {'type_code': 'L2', 'brand_code': 'H1', 'skin_code': 'D3', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S18', 'expression': 'L2 ∧ H1 ∧ D3 ∧ T6 ∧ G3 → S18'}, {'type_code': 'L2', 'brand_code': 'H1', 'skin_code': 'D4', 'size_code': 'T2', 'price_code': 'G2', 'product_id': 'S18', 'expression': 'L2 ∧ H1 ∧ D4 ∧ T2 ∧ G2 → S18'}, {'type_code': 'L2', 'brand_code': 'H1', 'skin_code': 'D4', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S18', 'expression': 'L2 ∧ H1 ∧ D4 ∧ T5 ∧ G3 → S18'}, {'type_code': 'L2', 'brand_code': 'H1', 'skin_code': 'D4', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S18', 'expression': 'L2 ∧ H1 ∧ D4 ∧ T6 ∧ G3 → S18'}, {'type_code': 'L2', 'brand_code': 'H12', 'skin_code': 'D3', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S19', 'expression': 'L2 ∧ H12 ∧ D3 ∧ T5 ∧ G3 → S19'}, {'type_code': 'L2', 'brand_code': 'H12', 'skin_code': 'D5', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S19', 'expression': 'L2 ∧ H12 ∧ D5 ∧ T5 ∧ G3 → S19'}, {'type_code': 'L2', 'brand_code': 'H12', 'skin_code': 'D7', 'size_code': 'T5', 'price_code': 'G3', 'product_id': 'S19', 'expression': 'L2 ∧ H12 ∧ D7 ∧ T5 ∧ G3 → S19'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D3', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D3 ∧ T4 ∧ G2 → S20'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D3', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D3 ∧ T6 ∧ G3 → S20'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D3', 'size_code': 'T7', 'price_code': 'G3', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D3 ∧ T7 ∧ G3 → S20'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D4', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D4 ∧ T4 ∧ G2 → S20'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D4', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D4 ∧ T6 ∧ G3 → S20'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D4', 'size_code': 'T7', 'price_code': 'G3', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D4 ∧ T7 ∧ G3 → S20'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D7', 'size_code': 'T4', 'price_code': 'G2', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D7 ∧ T4 ∧ G2 → S20'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D7', 'size_code': 'T6', 'price_code': 'G3', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D7 ∧ T6 ∧ G3 → S20'}, {'type_code': 'L2', 'brand_code': 'H6', 'skin_code': 'D7', 'size_code': 'T7', 'price_code': 'G3', 'product_id': 'S20', 'expression': 'L2 ∧ H6 ∧ D7 ∧ T7 ∧ G3 → S20'}, {'type_code': 'L3', 'brand_code': 'H13', 'skin_code': 'D1', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S21', 'expression': 'L3 ∧ H13 ∧ D1 ∧ T4 ∧ G3 → S21'}, {'type_code': 'L3', 'brand_code': 'H13', 'skin_code': 'D2', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S21', 'expression': 'L3 ∧ H13 ∧ D2 ∧ T4 ∧ G3 → S21'}, {'type_code': 'L3', 'brand_code': 'H13', 'skin_code': 'D3', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S21', 'expression': 'L3 ∧ H13 ∧ D3 ∧ T4 ∧ G3 → S21'}, {'type_code': 'L3', 'brand_code': 'H13', 'skin_code': 'D4', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S21', 'expression': 'L3 ∧ H13 ∧ D4 ∧ T4 ∧ G3 → S21'}, {'type_code': 'L3', 'brand_code': 'H13', 'skin_code': 'D5', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S21', 'expression': 'L3 ∧ H13 ∧ D5 ∧ T4 ∧ G3 → S21'}, {'type_code': 'L3', 'brand_code': 'H14', 'skin_code': 'D1', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S22', 'expression': 'L3 ∧ H14 ∧ D1 ∧ T9 ∧ G2 → S22'}, {'type_code': 'L3', 'brand_code': 'H14', 'skin_code': 'D2', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S22', 'expression': 'L3 ∧ H14 ∧ D2 ∧ T9 ∧ G2 → S22'}, {'type_code': 'L3', 'brand_code': 'H14', 'skin_code': 'D5', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S22', 'expression': 'L3 ∧ H14 ∧ D5 ∧ T9 ∧ G2 → S22'}, {'type_code': 'L3', 'brand_code': 'H14', 'skin_code': 'D1', 'size_code': 'T9', 'price_code': 'G3', 'product_id': 'S22', 'expression': 'L3 ∧ H14 ∧ D1 ∧ T9 ∧ G3 → S22'}, {'type_code': 'L3', 'brand_code': 'H14', 'skin_code': 'D2', 'size_code': 'T9', 'price_code': 'G3', 'product_id': 'S22', 'expression': 'L3 ∧ H14 ∧ D2 ∧ T9 ∧ G3 → S22'}, {'type_code': 'L3', 'brand_code': 'H14', 'skin_code': 'D5', 'size_code': 'T9', 'price_code': 'G3', 'product_id': 'S22', 'expression': 'L3 ∧ H14 ∧ D5 ∧ T9 ∧ G3 → S22'}, {'type_code': 'L3', 'brand_code': 'H15', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S23', 'expression': 'L3 ∧ H15 ∧ D1 ∧ T3 ∧ G4 → S23'}, {'type_code': 'L3', 'brand_code': 'H15', 'skin_code': 'D2', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S23', 'expression': 'L3 ∧ H15 ∧ D2 ∧ T3 ∧ G4 → S23'}, {'type_code': 'L3', 'brand_code': 'H15', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S23', 'expression': 'L3 ∧ H15 ∧ D3 ∧ T3 ∧ G4 → S23'}, {'type_code': 'L3', 'brand_code': 'H15', 'skin_code': 'D5', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S23', 'expression': 'L3 ∧ H15 ∧ D5 ∧ T3 ∧ G4 → S23'}, {'type_code': 'L3', 'brand_code': 'H16', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S24', 'expression': 'L3 ∧ H16 ∧ D1 ∧ T3 ∧ G4 → S24'}, {'type_code': 'L3', 'brand_code': 'H16', 'skin_code': 'D2', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S24', 'expression': 'L3 ∧ H16 ∧ D2 ∧ T3 ∧ G4 → S24'}, {'type_code': 'L3', 'brand_code': 'H16', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S24', 'expression': 'L3 ∧ H16 ∧ D3 ∧ T3 ∧ G4 → S24'}, {'type_code': 'L3', 'brand_code': 'H16', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S24', 'expression': 'L3 ∧ H16 ∧ D4 ∧ T3 ∧ G4 → S24'}, {'type_code': 'L3', 'brand_code': 'H16', 'skin_code': 'D5', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S24', 'expression': 'L3 ∧ H16 ∧ D5 ∧ T3 ∧ G4 → S24'}, {'type_code': 'L3', 'brand_code': 'H16', 'skin_code': 'D6', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S24', 'expression': 'L3 ∧ H16 ∧ D6 ∧ T3 ∧ G4 → S24'}, {'type_code': 'L3', 'brand_code': 'H9', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S25', 'expression': 'L3 ∧ H9 ∧ D1 ∧ T3 ∧ G2 → S25'}, {'type_code': 'L3', 'brand_code': 'H9', 'skin_code': 'D2', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S25', 'expression': 'L3 ∧ H9 ∧ D2 ∧ T3 ∧ G2 → S25'}, {'type_code': 'L3', 'brand_code': 'H9', 'skin_code': 'D1', 'size_code': 'T12', 'price_code': 'G4', 'product_id': 'S25', 'expression': 'L3 ∧ H9 ∧ D1 ∧ T12 ∧ G4 → S25'}, {'type_code': 'L3', 'brand_code': 'H9', 'skin_code': 'D2', 'size_code': 'T12', 'price_code': 'G4', 'product_id': 'S25', 'expression': 'L3 ∧ H9 ∧ D2 ∧ T12 ∧ G4 → S25'}, {'type_code': 'L3', 'brand_code': 'H6', 'skin_code': 'D2', 'size_code': 'T2', 'price_code': 'G2', 'product_id': 'S26', 'expression': 'L3 ∧ H6 ∧ D2 ∧ T2 ∧ G2 → S26'}, {'type_code': 'L3', 'brand_code': 'H6', 'skin_code': 'D2', 'size_code': 'T4', 'price_code': 'G3', 'product_id': 'S26', 'expression': 'L3 ∧ H6 ∧ D2 ∧ T4 ∧ G3 → S26'}, {'type_code': 'L3', 'brand_code': 'H10', 'skin_code': 'D1', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S27', 'expression': 'L3 ∧ H10 ∧ D1 ∧ T9 ∧ G2 → S27'}, {'type_code': 'L3', 'brand_code': 'H10', 'skin_code': 'D2', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S27', 'expression': 'L3 ∧ H10 ∧ D2 ∧ T9 ∧ G2 → S27'}, {'type_code': 'L3', 'brand_code': 'H10', 'skin_code': 'D3', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S27', 'expression': 'L3 ∧ H10 ∧ D3 ∧ T9 ∧ G2 → S27'}, {'type_code': 'L3', 'brand_code': 'H10', 'skin_code': 'D4', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S27', 'expression': 'L3 ∧ H10 ∧ D4 ∧ T9 ∧ G2 → S27'}, {'type_code': 'L3', 'brand_code': 'H10', 'skin_code': 'D5', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S27', 'expression': 'L3 ∧ H10 ∧ D5 ∧ T9 ∧ G2 → S27'}, {'type_code': 'L3', 'brand_code': 'H17', 'skin_code': 'D1', 'size_code': 'T1', 'price_code': 'G2', 'product_id': 'S28', 'expression': 'L3 ∧ H17 ∧ D1 ∧ T1 ∧ G2 → S28'}, {'type_code': 'L3', 'brand_code': 'H17', 'skin_code': 'D1', 'size_code': 'T1', 'price_code': 'G3', 'product_id': 'S28', 'expression': 'L3 ∧ H17 ∧ D1 ∧ T1 ∧ G3 → S28'}, {'type_code': 'L3', 'brand_code': 'H17', 'skin_code': 'D1', 'size_code': 'T2', 'price_code': 'G3', 'product_id': 'S28', 'expression': 'L3 ∧ H17 ∧ D1 ∧ T2 ∧ G3 → S28'}, {'type_code': 'L3', 'brand_code': 'H17', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S28', 'expression': 'L3 ∧ H17 ∧ D1 ∧ T3 ∧ G4 → S28'}, {'type_code': 'L3', 'brand_code': 'H17', 'skin_code': 'D2', 'size_code': 'T1', 'price_code': 'G2', 'product_id': 'S28', 'expression': 'L3 ∧ H17 ∧ D2 ∧ T1 ∧ G2 → S28'}, {'type_code': 'L3', 'brand_code': 'H17', 'skin_code': 'D2', 'size_code': 'T1', 'price_code': 'G3', 'product_id': 'S28', 'expression': 'L3 ∧ H17 ∧ D2 ∧ T1 ∧ G3 → S28'}, {'type_code': 'L3', 'brand_code': 'H17', 'skin_code': 'D2', 'size_code': 'T2', 'price_code': 'G3', 'product_id': 'S28', 'expression': 'L3 ∧ H17 ∧ D2 ∧ T2 ∧ G3 → S28'}, {'type_code': 'L3', 'brand_code': 'H17', 'skin_code': 'D2', 'size_code': 'T3', 'price_code': 'G4', 'product_id': 'S28', 'expression': 'L3 ∧ H17 ∧ D2 ∧ T3 ∧ G4 → S28'}, {'type_code': 'L3', 'brand_code': 'H2', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S29', 'expression': 'L3 ∧ H2 ∧ D1 ∧ T3 ∧ G2 → S29'}, {'type_code': 'L3', 'brand_code': 'H2', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S29', 'expression': 'L3 ∧ H2 ∧ D3 ∧ T3 ∧ G2 → S29'}, {'type_code': 'L3', 'brand_code': 'H2', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G2', 'product_id': 'S29', 'expression': 'L3 ∧ H2 ∧ D4 ∧ T3 ∧ G2 → S29'}, {'type_code': 'L3', 'brand_code': 'H18', 'skin_code': 'D1', 'size_code': 'T12', 'price_code': 'G2', 'product_id': 'S30', 'expression': 'L3 ∧ H18 ∧ D1 ∧ T12 ∧ G2 → S30'}, {'type_code': 'L3', 'brand_code': 'H18', 'skin_code': 'D2', 'size_code': 'T12', 'price_code': 'G2', 'product_id': 'S30', 'expression': 'L3 ∧ H18 ∧ D2 ∧ T12 ∧ G2 → S30'}, {'type_code': 'L3', 'brand_code': 'H18', 'skin_code': 'D4', 'size_code': 'T12', 'price_code': 'G2', 'product_id': 'S30', 'expression': 'L3 ∧ H18 ∧ D4 ∧ T12 ∧ G2 → S30'}, {'type_code': 'L4', 'brand_code': 'H16', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S31', 'expression': 'L4 ∧ H16 ∧ D1 ∧ T3 ∧ G3 → S31'}, {'type_code': 'L4', 'brand_code': 'H16', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S31', 'expression': 'L4 ∧ H16 ∧ D3 ∧ T3 ∧ G3 → S31'}, {'type_code': 'L4', 'brand_code': 'H16', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S31', 'expression': 'L4 ∧ H16 ∧ D4 ∧ T3 ∧ G3 → S31'}, {'type_code': 'L4', 'brand_code': 'H3', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S32', 'expression': 'L4 ∧ H3 ∧ D1 ∧ T3 ∧ G3 → S32'}, {'type_code': 'L4', 'brand_code': 'H3', 'skin_code': 'D2', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S32', 'expression': 'L4 ∧ H3 ∧ D2 ∧ T3 ∧ G3 → S32'}, {'type_code': 'L4', 'brand_code': 'H3', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S32', 'expression': 'L4 ∧ H3 ∧ D3 ∧ T3 ∧ G3 → S32'}, {'type_code': 'L4', 'brand_code': 'H3', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S32', 'expression': 'L4 ∧ H3 ∧ D4 ∧ T3 ∧ G3 → S32'}, {'type_code': 'L4', 'brand_code': 'H19', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S33', 'expression': 'L4 ∧ H19 ∧ D1 ∧ T3 ∧ G3 → S33'}, {'type_code': 'L4', 'brand_code': 'H19', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S33', 'expression': 'L4 ∧ H19 ∧ D4 ∧ T3 ∧ G3 → S33'}, {'type_code': 'L4', 'brand_code': 'H19', 'skin_code': 'D5', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S33', 'expression': 'L4 ∧ H19 ∧ D5 ∧ T3 ∧ G3 → S33'}, {'type_code': 'L4', 'brand_code': 'H20', 'skin_code': 'D1', 'size_code': 'T2', 'price_code': 'G3', 'product_id': 'S34', 'expression': 'L4 ∧ H20 ∧ D1 ∧ T2 ∧ G3 → S34'}, {'type_code': 'L4', 'brand_code': 'H20', 'skin_code': 'D2', 'size_code': 'T2', 'price_code': 'G3', 'product_id': 'S34', 'expression': 'L4 ∧ H20 ∧ D2 ∧ T2 ∧ G3 → S34'}, {'type_code': 'L4', 'brand_code': 'H20', 'skin_code': 'D3', 'size_code': 'T2', 'price_code': 'G3', 'product_id': 'S34', 'expression': 'L4 ∧ H20 ∧ D3 ∧ T2 ∧ G3 → S34'}, {'type_code': 'L4', 'brand_code': 'H20', 'skin_code': 'D4', 'size_code': 'T2', 'price_code': 'G3', 'product_id': 'S34', 'expression': 'L4 ∧ H20 ∧ D4 ∧ T2 ∧ G3 → S34'}, {'type_code': 'L4', 'brand_code': 'H20', 'skin_code': 'D5', 'size_code': 'T2', 'price_code': 'G3', 'product_id': 'S34', 'expression': 'L4 ∧ H20 ∧ D5 ∧ T2 ∧ G3 → S34'}, {'type_code': 'L4', 'brand_code': 'H21', 'skin_code': 'D1', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S35', 'expression': 'L4 ∧ H21 ∧ D1 ∧ T9 ∧ G2 → S35'}, {'type_code': 'L4', 'brand_code': 'H21', 'skin_code': 'D3', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S35', 'expression': 'L4 ∧ H21 ∧ D3 ∧ T9 ∧ G2 → S35'}, {'type_code': 'L4', 'brand_code': 'H21', 'skin_code': 'D4', 'size_code': 'T9', 'price_code': 'G2', 'product_id': 'S35', 'expression': 'L4 ∧ H21 ∧ D4 ∧ T9 ∧ G2 → S35'}, {'type_code': 'L4', 'brand_code': 'H21', 'skin_code': 'D1', 'size_code': 'T9', 'price_code': 'G3', 'product_id': 'S35', 'expression': 'L4 ∧ H21 ∧ D1 ∧ T9 ∧ G3 → S35'}, {'type_code': 'L4', 'brand_code': 'H21', 'skin_code': 'D3', 'size_code': 'T9', 'price_code': 'G3', 'product_id': 'S35', 'expression': 'L4 ∧ H21 ∧ D3 ∧ T9 ∧ G3 → S35'}, {'type_code': 'L4', 'brand_code': 'H21', 'skin_code': 'D4', 'size_code': 'T9', 'price_code': 'G3', 'product_id': 'S35', 'expression': 'L4 ∧ H21 ∧ D4 ∧ T9 ∧ G3 → S35'}, {'type_code': 'L4', 'brand_code': 'H5', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S36', 'expression': 'L4 ∧ H5 ∧ D3 ∧ T3 ∧ G3 → S36'}, {'type_code': 'L4', 'brand_code': 'H5', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S36', 'expression': 'L4 ∧ H5 ∧ D4 ∧ T3 ∧ G3 → S36'}, {'type_code': 'L4', 'brand_code': 'H5', 'skin_code': 'D5', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S36', 'expression': 'L4 ∧ H5 ∧ D5 ∧ T3 ∧ G3 → S36'}, {'type_code': 'L4', 'brand_code': 'H5', 'skin_code': 'D7', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S36', 'expression': 'L4 ∧ H5 ∧ D7 ∧ T3 ∧ G3 → S36'}, {'type_code': 'L4', 'brand_code': 'H15', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S37', 'expression': 'L4 ∧ H15 ∧ D3 ∧ T3 ∧ G3 → S37'}, {'type_code': 'L4', 'brand_code': 'H15', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S37', 'expression': 'L4 ∧ H15 ∧ D4 ∧ T3 ∧ G3 → S37'}, {'type_code': 'L4', 'brand_code': 'H15', 'skin_code': 'D5', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S37', 'expression': 'L4 ∧ H15 ∧ D5 ∧ T3 ∧ G3 → S37'}, {'type_code': 'L4', 'brand_code': 'H15', 'skin_code': 'D7', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S37', 'expression': 'L4 ∧ H15 ∧ D7 ∧ T3 ∧ G3 → S37'}, {'type_code': 'L4', 'brand_code': 'H22', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S38', 'expression': 'L4 ∧ H22 ∧ D1 ∧ T3 ∧ G3 → S38'}, {'type_code': 'L4', 'brand_code': 'H22', 'skin_code': 'D2', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S38', 'expression': 'L4 ∧ H22 ∧ D2 ∧ T3 ∧ G3 → S38'}, {'type_code': 'L4', 'brand_code': 'H22', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S38', 'expression': 'L4 ∧ H22 ∧ D3 ∧ T3 ∧ G3 → S38'}, {'type_code': 'L4', 'brand_code': 'H22', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S38', 'expression': 'L4 ∧ H22 ∧ D4 ∧ T3 ∧ G3 → S38'}, {'type_code': 'L4', 'brand_code': 'H6', 'skin_code': 'D5', 'size_code': 'T1', 'price_code': 'G2', 'product_id': 'S39', 'expression': 'L4 ∧ H6 ∧ D5 ∧ T1 ∧ G2 → S39'}, {'type_code': 'L4', 'brand_code': 'H6', 'skin_code': 'D5', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S39', 'expression': 'L4 ∧ H6 ∧ D5 ∧ T3 ∧ G3 → S39'}, {'type_code': 'L4', 'brand_code': 'H13', 'skin_code': 'D1', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S40', 'expression': 'L4 ∧ H13 ∧ D1 ∧ T3 ∧ G3 → S40'}, {'type_code': 'L4', 'brand_code': 'H13', 'skin_code': 'D2', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S40', 'expression': 'L4 ∧ H13 ∧ D2 ∧ T3 ∧ G3 → S40'}, {'type_code': 'L4', 'brand_code': 'H13', 'skin_code': 'D3', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S40', 'expression': 'L4 ∧ H13 ∧ D3 ∧ T3 ∧ G3 → S40'}, {'type_code': 'L4', 'brand_code': 'H13', 'skin_code': 'D4', 'size_code': 'T3', 'price_code': 'G3', 'product_id': 'S40', 'expression': 'L4 ∧ H13 ∧ D4 ∧ T3 ∧ G3 → S40'}]


def get_products_for_filters(skin_type, product_type, brand="Tất cả"):
    """Lấy sản phẩm khớp với loại da, nhóm sản phẩm và thương hiệu."""
    matched = []
    for product in PRODUCTS:
        if product_type != "Tất cả" and product["type"] != product_type:
            continue
        if skin_type != "Tất cả" and skin_type not in product["skin_types"]:
            continue
        if brand != "Tất cả":
            same_brand = product["brand"] == brand
            if brand == "La Roche-Posay" and product["brand"] == "La Roche Posay":
                same_brand = True
            if brand in ("d'Alba", "d’ Alba") and product["brand"] in ("d'Alba", "d’ Alba"):
                same_brand = True
            if not same_brand:
                continue
        matched.append(product)
    return matched


def get_variants_for_filters(products):
    """Lấy các biến thể dung tích/giá thuộc những sản phẩm đang phù hợp."""
    variants = []
    for product in products:
        for variant in product["variants"]:
            if variant.get("size") is None:
                continue
            variants.append(variant)
    return variants


st.title("🌿 HỆ CHUYÊN GIA TƯ VẤN SẢN PHẨM CHĂM SÓC DA MẶT")
st.caption("Nhóm 13 – Nhập môn Trí tuệ nhân tạo")

with st.container(border=True):
    st.subheader("Thông tin tư vấn")
    c1, c2, c3 = st.columns(3)

    with c1:
        selected_skin = st.selectbox(
            "Loại da phù hợp",
            ["Tất cả", "Da thường", "Da khô", "Da dầu", "Da hỗn hợp",
             "Da nhạy cảm", "Da đang điều trị", "Da mụn"],
            key="selected_skin",
        )
        selected_type = st.selectbox(
            "Nhóm sản phẩm",
            ["Tất cả", "Nước tẩy trang", "Sữa rửa mặt", "Kem dưỡng", "Kem chống nắng"],
            key="selected_type",
        )

    # Bước 1: chỉ liệt kê thương hiệu có sản phẩm khớp loại da + nhóm sản phẩm.
    products_for_brand = get_products_for_filters(selected_skin, selected_type)
    available_brands = sorted(
        {product["brand"] for product in products_for_brand},
        key=lambda value: value.casefold(),
    )
    brand_options = ["Tất cả"] + available_brands
    if st.session_state.get("selected_brand", "Tất cả") not in brand_options:
        st.session_state["selected_brand"] = "Tất cả"

    with c2:
        selected_brand = st.selectbox(
            "Thương hiệu",
            brand_options,
            key="selected_brand",
        )

    # Bước 2: lấy sản phẩm theo loại da + nhóm sản phẩm + thương hiệu.
    products_for_price_size = get_products_for_filters(
        selected_skin, selected_type, selected_brand
    )
    variants_for_price_size = get_variants_for_filters(products_for_price_size)

    # Bước 3: chỉ hiển thị khoảng giá có mặt trong các sản phẩm đang phù hợp.
    available_prices = sorted(
        {get_price_code(variant["price"]) for variant in variants_for_price_size},
        key=lambda code: int(code[1:]),
    )
    price_options = ["Tất cả"] + available_prices
    if st.session_state.get("selected_price", "Tất cả") not in price_options:
        st.session_state["selected_price"] = "Tất cả"

    with c3:
        selected_price = st.selectbox(
            "Khoảng giá",
            price_options,
            format_func=lambda code: "Tất cả mức giá" if code == "Tất cả" else PRICE_LABELS.get(code, code),
            key="selected_price",
        )

    # Bước 4: dung tích phụ thuộc cả các tiêu chí trước đó và khoảng giá.
    variants_for_size = [
        variant for variant in variants_for_price_size
        if selected_price == "Tất cả" or get_price_code(variant["price"]) == selected_price
    ]
    available_size_codes = sorted(
        {get_size_code(variant["size"], variant["unit"]) for variant in variants_for_size},
        key=lambda code: int(code[1:]) if code.startswith("T") and code[1:].isdigit() else 99,
    )
    size_options = ["Tất cả"] + available_size_codes
    if st.session_state.get("selected_size", "Tất cả") not in size_options:
        st.session_state["selected_size"] = "Tất cả"

    selected_size = st.selectbox(
        "Khoảng dung tích",
        size_options,
        format_func=lambda code: "Tất cả dung tích" if code == "Tất cả" else SIZE_LABELS.get(code, code),
        key="selected_size",
    )

    search_clicked = st.button(
        "🔎 Tư vấn sản phẩm", type="primary", use_container_width=True
    )

if search_clicked:
    results = infer_products(
        selected_skin, selected_type, selected_brand, selected_size, selected_price
    )
    st.session_state["consultation_results"] = results
    st.session_state["consultation_criteria"] = {
        "skin": selected_skin,
        "type": selected_type,
        "brand": selected_brand,
        "size": selected_size,
        "price": selected_price,
    }

if "consultation_results" in st.session_state:
    results = st.session_state["consultation_results"]
    st.divider()
    st.subheader(f"Kết quả tư vấn: {len(results)} sản phẩm phù hợp")

    if not results:
        st.warning(
            "Không tìm thấy sản phẩm phù hợp với tất cả tiêu chí đã chọn. "
            "Bạn hãy thử đổi một hoặc nhiều tiêu chí."
        )
    else:
        st.info(
            "Giá chỉ mang tính tham khảo và có thể thay đổi theo nơi bán."
        )
        for item in results:
            product = item["product"]
            with st.container(border=True):
                left, right = st.columns([1, 3])
                with left:
                    image_path = Path("anh") / f"{product['id']}.png"
                    if image_path.exists():
                        st.image(str(image_path), use_container_width=True)
                    else:
                        st.markdown(f"### {product['id']}")
                        st.caption("Có thể thêm ảnh vào thư mục images")
                with right:
                    st.markdown(f"### {product['name']}")
                    st.write(
                        f"**Nhóm:** {product['type']}"
                    )
                    st.write(
                        f"**Thương hiệu:** {product['brand']}"
                    )
                    
                    st.write(
                        "**Loại da trong cơ sở tri thức:** "
                        + (", ".join(product["skin_types"]) if product["skin_types"] else "Chưa cập nhật")
                    )
                    if product["description"]:
                        st.write(product["description"])
                    st.markdown("**Dung tích và giá phù hợp:**")
                    for v in item["variants"]:
                        st.write(f"- {format_size(v)} — **{format_money(v['price'])}**")

