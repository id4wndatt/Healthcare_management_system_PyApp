-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th7 08, 2024 lúc 04:31 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `hcms`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hcms_danhmuc_dichvu`
--

CREATE TABLE `hcms_danhmuc_dichvu` (
  `id` int(11) NOT NULL,
  `dm_dv_ten` varchar(255) DEFAULT NULL,
  `dm_dv_mota` longtext DEFAULT NULL,
  `dm_dv_trangthai` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `hcms_danhmuc_dichvu`
--

INSERT INTO `hcms_danhmuc_dichvu` (`id`, `dm_dv_ten`, `dm_dv_mota`, `dm_dv_trangthai`) VALUES
(1, 'Gói điều trị và chăm sóc bệnh tật', 'Các dịch vụ y tế và điều trị cho các bệnh lý cụ thể.', 1),
(2, 'Gói khám sức khỏe định kỳ', 'Bao gồm các xét nghiệm và kiểm tra định kỳ để phát hiện sớm các vấn đề sức khỏe.', 1),
(3, 'Gói dịch vụ chăm sóc sức khỏe cho người cao tuổi', 'Các dịch vụ chuyên biệt cho người cao tuổi, bao gồm cả chăm sóc tại nhà và khám sức khỏe định kỳ.', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hcms_dichvu`
--

CREATE TABLE `hcms_dichvu` (
  `id` int(11) NOT NULL,
  `dv_ten` varchar(255) DEFAULT NULL,
  `dv_dongia` double DEFAULT NULL,
  `dv_mota` longtext DEFAULT NULL,
  `dv_trangthai` tinyint(1) DEFAULT NULL,
  `dv_danhmuc_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `hcms_dichvu`
--

INSERT INTO `hcms_dichvu` (`id`, `dv_ten`, `dv_dongia`, `dv_mota`, `dv_trangthai`, `dv_danhmuc_id`) VALUES
(5, 'Khám và điều trị bệnh lý', 690000, 'Bao gồm các cuộc khám sức khỏe chi tiết, chẩn đoán và lựa chọn phương pháp điều trị phù hợp.', 1, 1),
(6, 'Thuốc và liệu pháp điều trị', 490000, 'Bao gồm việc cung cấp thuốc điều trị, liệu pháp vật lý, liệu pháp phục hồi chức năng, và các liệu pháp khác như hóa trị, phẫu thuật nếu cần thiết.', 1, 1),
(7, 'Xét nghiệm và chẩn đoán hình ảnh', 390000, 'Các loại xét nghiệm máu, xét nghiệm hóa sinh, siêu âm, chụp X-quang, MRI, CT-scan để xác định bệnh lý và theo dõi quá trình điều trị.', 1, 1),
(8, 'Khám lâm sàng tổng quát', 290000, 'Đo huyết áp, Đo chiều cao, cân nặng, chỉ số BMI, Khám tim mạch, Khám hô hấp, Khám nội tiết, Khám tiêu hóa', 1, 2),
(9, 'Tư vấn sức khỏe', 190000, 'Tư vấn về lối sống lành mạnh, Hướng dẫn cách phòng ngừa bệnh tật, Đánh giá và hướng dẫn các biện pháp cải thiện sức khỏe', 1, 2),
(10, 'Khám và theo dõi bệnh lý mãn tính', 350000, 'Theo dõi và điều trị các bệnh mãn tính như tiểu đường, cao huyết áp, bệnh tim mạch, bệnh phổi mãn tính, Điều chỉnh và theo dõi việc sử dụng thuốc', 1, 3),
(11, 'Phục hồi chức năng và vật lý trị liệu', 450000, 'Các chương trình phục hồi chức năng cho người bị đột quỵ, viêm khớp, thoái hóa khớp, Vật lý trị liệu để cải thiện khả năng vận động, giảm đau', 1, 3);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hcms_hoadon`
--

CREATE TABLE `hcms_hoadon` (
  `id` int(11) NOT NULL,
  `hd_tongtien` double DEFAULT NULL,
  `hd_ngaygiotao` datetime DEFAULT NULL,
  `hd_trangthai` tinyint(1) DEFAULT NULL,
  `hd_mota` longtext DEFAULT NULL,
  `hd_khachhang_id` int(11) DEFAULT NULL,
  `hd_nhanvien_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `hcms_hoadon`
--

INSERT INTO `hcms_hoadon` (`id`, `hd_tongtien`, `hd_ngaygiotao`, `hd_trangthai`, `hd_mota`, `hd_khachhang_id`, `hd_nhanvien_id`) VALUES
(17, 290000, '2024-07-03 10:00:00', 1, 'Đo huyết áp, Đo chiều cao, cân nặng', 1, 2),
(19, 390000, '2024-06-07 14:00:00', 1, 'Các loại xét nghiệm máu, xét nghiệm hóa sinh', 1, 2),
(20, 1350000, '2024-07-07 09:00:00', 1, 'Các chương trình phục hồi chức năng cho người bị đột quỵ, viêm khớp, thoái hóa khớp', 1, 2),
(21, 380000, '2024-08-07 09:00:00', 1, 'Tư vấn về lối sống lành mạnh, Hướng dẫn cách phòng ngừa bệnh tật, Đánh giá và hướng dẫn các biện pháp cải thiện sức khỏe', 1, 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hcms_hoadon_chitiet`
--

CREATE TABLE `hcms_hoadon_chitiet` (
  `id` int(11) NOT NULL,
  `hdct_soluong` int(11) DEFAULT NULL,
  `hdct_dichvu_id` int(11) DEFAULT NULL,
  `hdct_hoadon_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `hcms_hoadon_chitiet`
--

INSERT INTO `hcms_hoadon_chitiet` (`id`, `hdct_soluong`, `hdct_dichvu_id`, `hdct_hoadon_id`) VALUES
(10, 1, 8, 17),
(12, 1, 7, 19),
(13, 3, 11, 20),
(14, 2, 9, 21);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hcms_khachhang`
--

CREATE TABLE `hcms_khachhang` (
  `id` int(11) NOT NULL,
  `kh_hoten` varchar(255) DEFAULT NULL,
  `kh_gioitinh` tinyint(1) DEFAULT NULL,
  `kh_sdt` varchar(10) DEFAULT NULL,
  `kh_ngaysinh` date DEFAULT NULL,
  `kh_diachi` varchar(255) DEFAULT NULL,
  `kh_trangthai` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `hcms_khachhang`
--

INSERT INTO `hcms_khachhang` (`id`, `kh_hoten`, `kh_gioitinh`, `kh_sdt`, `kh_ngaysinh`, `kh_diachi`, `kh_trangthai`) VALUES
(1, 'Đào Ngọc Bích', 0, '0846836449', '2004-09-27', 'Thái Bình', 1),
(3, 'Bùi Ngọc Đức', 1, '0999888999', '2002-12-26', 'Hòa Bình', 1),
(4, 'Nguyễn Thanh Tùng', 1, '0876394757', '2000-10-10', 'Thái Bình', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hcms_lichhen`
--

CREATE TABLE `hcms_lichhen` (
  `id` int(11) NOT NULL,
  `lh_ngayhen` datetime DEFAULT NULL,
  `lh_trangthai` tinyint(1) DEFAULT NULL,
  `lh_khachhang_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `hcms_lichhen`
--

INSERT INTO `hcms_lichhen` (`id`, `lh_ngayhen`, `lh_trangthai`, `lh_khachhang_id`) VALUES
(11, '2024-07-04 12:00:00', 1, 1),
(12, '2024-07-06 12:00:00', 0, 3),
(13, '2024-07-07 09:00:00', 0, 1),
(14, '2024-07-05 14:00:00', 0, 3),
(15, '2024-07-06 13:01:00', 0, 3),
(16, '2024-07-01 15:00:00', 0, 4);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hcms_nhanvien`
--

CREATE TABLE `hcms_nhanvien` (
  `id` int(11) NOT NULL,
  `nv_hoten` varchar(255) DEFAULT NULL,
  `nv_gioitinh` tinyint(1) DEFAULT NULL,
  `nv_sdt` varchar(10) DEFAULT NULL,
  `nv_ngaysinh` date DEFAULT NULL,
  `nv_diachi` varchar(255) DEFAULT NULL,
  `nv_chucvu` tinyint(1) DEFAULT NULL,
  `nv_trangthai` tinyint(1) DEFAULT NULL,
  `nv_matkhau` varchar(255) DEFAULT NULL,
  `nv_quyen` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `hcms_nhanvien`
--

INSERT INTO `hcms_nhanvien` (`id`, `nv_hoten`, `nv_gioitinh`, `nv_sdt`, `nv_ngaysinh`, `nv_diachi`, `nv_chucvu`, `nv_trangthai`, `nv_matkhau`, `nv_quyen`) VALUES
(1, 'Đàm Như Đạt', 1, '1', '2003-03-31', 'Sơn La', 0, 1, '1', 0),
(2, 'Vũ Minh Chiến', 1, '0862539888', '2003-07-16', 'Hòa Bình', 0, 1, '1', 0),
(10, 'Bùi Ngọc Đức', 1, '12', '2003-12-22', 'Hòa Bình', 1, 1, '1', 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `hcms_danhmuc_dichvu`
--
ALTER TABLE `hcms_danhmuc_dichvu`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `hcms_dichvu`
--
ALTER TABLE `hcms_dichvu`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_dichvu_danhmuc` (`dv_danhmuc_id`);

--
-- Chỉ mục cho bảng `hcms_hoadon`
--
ALTER TABLE `hcms_hoadon`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_hoadon_khachhang` (`hd_khachhang_id`),
  ADD KEY `fk_hoadon_nhanvien` (`hd_nhanvien_id`);

--
-- Chỉ mục cho bảng `hcms_hoadon_chitiet`
--
ALTER TABLE `hcms_hoadon_chitiet`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_chitiethoadon_hoadon` (`hdct_hoadon_id`),
  ADD KEY `fk_chititethoadon_dichvu` (`hdct_dichvu_id`);

--
-- Chỉ mục cho bảng `hcms_khachhang`
--
ALTER TABLE `hcms_khachhang`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `hcms_lichhen`
--
ALTER TABLE `hcms_lichhen`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_lichhen_khachhang` (`lh_khachhang_id`);

--
-- Chỉ mục cho bảng `hcms_nhanvien`
--
ALTER TABLE `hcms_nhanvien`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `hcms_danhmuc_dichvu`
--
ALTER TABLE `hcms_danhmuc_dichvu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `hcms_dichvu`
--
ALTER TABLE `hcms_dichvu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT cho bảng `hcms_hoadon`
--
ALTER TABLE `hcms_hoadon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT cho bảng `hcms_hoadon_chitiet`
--
ALTER TABLE `hcms_hoadon_chitiet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT cho bảng `hcms_khachhang`
--
ALTER TABLE `hcms_khachhang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT cho bảng `hcms_lichhen`
--
ALTER TABLE `hcms_lichhen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT cho bảng `hcms_nhanvien`
--
ALTER TABLE `hcms_nhanvien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `hcms_dichvu`
--
ALTER TABLE `hcms_dichvu`
  ADD CONSTRAINT `fk_dichvu_danhmuc` FOREIGN KEY (`dv_danhmuc_id`) REFERENCES `hcms_danhmuc_dichvu` (`id`);

--
-- Các ràng buộc cho bảng `hcms_hoadon`
--
ALTER TABLE `hcms_hoadon`
  ADD CONSTRAINT `fk_hoadon_khachhang` FOREIGN KEY (`hd_khachhang_id`) REFERENCES `hcms_khachhang` (`id`),
  ADD CONSTRAINT `fk_hoadon_nhanvien` FOREIGN KEY (`hd_nhanvien_id`) REFERENCES `hcms_nhanvien` (`id`);

--
-- Các ràng buộc cho bảng `hcms_hoadon_chitiet`
--
ALTER TABLE `hcms_hoadon_chitiet`
  ADD CONSTRAINT `fk_chitiethoadon_hoadon` FOREIGN KEY (`hdct_hoadon_id`) REFERENCES `hcms_hoadon` (`id`),
  ADD CONSTRAINT `fk_chititethoadon_dichvu` FOREIGN KEY (`hdct_dichvu_id`) REFERENCES `hcms_dichvu` (`id`);

--
-- Các ràng buộc cho bảng `hcms_lichhen`
--
ALTER TABLE `hcms_lichhen`
  ADD CONSTRAINT `fk_lichhen_khachhang` FOREIGN KEY (`lh_khachhang_id`) REFERENCES `hcms_khachhang` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
