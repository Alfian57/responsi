-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Dec 30, 2024 at 06:28 AM
-- Server version: 8.3.0
-- PHP Version: 8.2.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `responsi_5230411121`
--

-- --------------------------------------------------------

--
-- Table structure for table `produk`
--

CREATE TABLE `produk` (
  `id_produk` int NOT NULL,
  `nama_produk` varchar(255) NOT NULL,
  `harga` decimal(10,2) NOT NULL
) ENGINE=InnoDB;

--
-- Dumping data for table `produk`
--

INSERT INTO `produk` (`id_produk`, `nama_produk`, `harga`) VALUES
(1, 'Processor AMD Ryzen 3 3200u', 1500000.00),
(2, 'Processor AMD Ryzen 5 3200u', 1700000.00),
(3, 'Processor AMD Ryzen 7 3200u', 1800000.00),
(4, 'Processor AMD Ryzen 5 5200u', 2000000.00),
(5, 'RAM 2GB 2400MHz DDR4', 250000.00),
(6, 'RAM 4GB 2400MHz DDR4', 300000.00),
(7, 'RAM 8GB 2400MHz DDR4', 400000.00),
(8, 'RAM 2GB 3200MHz DDR4', 250000.00),
(9, 'RAM 4GB 3200MHz DDR4', 350000.00),
(10, 'RAM 8GB 3200MHz DDR4', 450000.00),
(11, 'SSD SATA 128GB', 200000.00),
(12, 'SSD SATA 256GB', 250000.00),
(13, 'SSD SATA 512GB', 300000.00),
(14, 'SSD SATA 1TB', 350000.00),
(15, 'SSD M.2 NVMe 128GB', 300000.00),
(16, 'SSD M.2 NVMe 256GB', 350000.00),
(17, 'SSD M.2 NVMe 512GB', 400000.00),
(18, 'SSD M.2 NVMe 1TB', 450000.00),
(19, 'Harddisk 512GB', 250000.00),
(20, 'Harddisk 1TB', 400000.00),
(21, 'Mechanical Keyboard GAMEN TITAN V RGB', 300000.00);

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int NOT NULL,
  `id_produk` int NOT NULL,
  `jumlah` int NOT NULL,
  `total_harga` decimal(10,2) NOT NULL,
  `tanggal_transaksi` date NOT NULL
) ENGINE=InnoDB;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_produk`, `jumlah`, `total_harga`, `tanggal_transaksi`) VALUES
(1, 20, 2, 800000.00, '2024-12-17'),
(2, 17, 3, 1200000.00, '2024-12-18'),
(3, 1, 1, 1500000.00, '2024-12-17'),
(4, 6, 10, 3000000.00, '2024-12-18'),
(5, 6, 4, 1800000.00, '2024-12-18'),
(6, 10, 2, 900000.00, '2024-12-11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `produk`
--
ALTER TABLE `produk`
  ADD PRIMARY KEY (`id_produk`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_produk` (`id_produk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `produk`
--
ALTER TABLE `produk`
  MODIFY `id_produk` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`id_produk`) REFERENCES `produk` (`id_produk`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
