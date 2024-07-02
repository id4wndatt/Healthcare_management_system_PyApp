-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th7 02, 2024 lúc 06:10 PM
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

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hcms_lichhen`
--

CREATE TABLE `hcms_lichhen` (
  `id` int(11) NOT NULL,
  `lh_ngayhen` date DEFAULT NULL,
  `lh_giohen` time DEFAULT NULL,
  `lh_trangthai` tinyint(1) DEFAULT NULL,
  `lh_khachhang_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

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
  `nv_chucvu` varchar(255) DEFAULT NULL,
  `nv_trangthai` tinyint(1) DEFAULT NULL,
  `nv_matkhau` varchar(255) DEFAULT NULL,
  `nv_quyen` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `hcms_dichvu`
--
ALTER TABLE `hcms_dichvu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `hcms_hoadon`
--
ALTER TABLE `hcms_hoadon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `hcms_hoadon_chitiet`
--
ALTER TABLE `hcms_hoadon_chitiet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `hcms_khachhang`
--
ALTER TABLE `hcms_khachhang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `hcms_lichhen`
--
ALTER TABLE `hcms_lichhen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `hcms_nhanvien`
--
ALTER TABLE `hcms_nhanvien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
