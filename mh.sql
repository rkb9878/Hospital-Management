-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2019 at 05:19 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mh`
--

-- --------------------------------------------------------

--
-- Table structure for table `dischargedata`
--

CREATE TABLE `dischargedata` (
  `number` varchar(30) NOT NULL,
  `dateofadmission` date NOT NULL,
  `timeofadmission` time NOT NULL,
  `dateofdischarge` date NOT NULL,
  `timeofdischarge` time NOT NULL,
  `n_patient` varchar(100) NOT NULL,
  `ward` varchar(15) NOT NULL,
  `injuryreport` varchar(200) NOT NULL,
  `medicalcategory` varchar(200) NOT NULL,
  `disposal` varchar(200) NOT NULL,
  `disposedas` varchar(200) NOT NULL,
  `documentinitiated` varchar(200) NOT NULL,
  `medicalboardheldon` varchar(200) NOT NULL,
  `medicalboarddueon` varchar(100) NOT NULL,
  `medicalboarddesc` text NOT NULL,
  `diagnosis` text NOT NULL,
  `summary` text NOT NULL,
  `instructiontopatient` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dischargedata`
--

INSERT INTO `dischargedata` (`number`, `dateofadmission`, `timeofadmission`, `dateofdischarge`, `timeofdischarge`, `n_patient`, `ward`, `injuryreport`, `medicalcategory`, `disposal`, `disposedas`, `documentinitiated`, `medicalboardheldon`, `medicalboarddueon`, `medicalboarddesc`, `diagnosis`, `summary`, `instructiontopatient`) VALUES
('13993255-H', '2019-01-14', '15:00:00', '2019-01-14', '15:03:58', 'ANJALI SINGH', 'F-3', '14/01/19', 'SHAPE 1', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A\n', '-DIAGNOSED WITH COLD AND AMNESIA\n-DIAGNOSED WITH MILD ASTHMA\n', 'PATIENT RECEIVED AS SEVERLY ILL. FURTHUR DIAGNOSIS REVEALED MILD ASTHMA AND AMNESIA. PATIENT GIVEN GLUCOSE IP300 AND NUBILISATION 250 ML WITH 2 DOSE.\n', 'N/A\n'),
('13993255-H', '2019-06-07', '11:23:00', '2019-06-07', '11:30:43', 'rahul', 'sd', 'jjf', 'vdvi', 'vjdsi', 'vjdsi', 'vjdsif', 'vjdi', 'vdsjiv', 'diu\ndv\nd\nsd\n', 'sdfs\ndvds\n\n', 'dfvsdv\ndvd\n	cvb\n', 'gdg\ndvd\ndvd\n'),
('13993255-H', '2019-06-08', '11:03:00', '2019-06-08', '11:04:31', 'rah', 'na', 'n.a', 'n/aq', 'na/', 'n/aq', 'n/aq', 'n/aq', 'n/aq', 'n/aq\nn/aq\nn/aq\nn/aq\n\nn/aq\n', 'n/aq\nn/aq\nn/aq\n', 'n/aqn/aq\n\n', 'n/aq\n');

-- --------------------------------------------------------

--
-- Table structure for table `officialdata`
--

CREATE TABLE `officialdata` (
  `number` varchar(30) NOT NULL,
  `h_name` varchar(50) NOT NULL,
  `adno` varchar(20) NOT NULL,
  `rank` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `unitwaddress` varchar(50) NOT NULL,
  `service` varchar(10) NOT NULL,
  `station` varchar(30) NOT NULL,
  `command` varchar(30) NOT NULL,
  `nkin` varchar(30) NOT NULL,
  `relation` varchar(20) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `cdano` varchar(20) NOT NULL,
  `roffice` varchar(30) NOT NULL,
  `addroffice` varchar(50) NOT NULL,
  `totals` varchar(7) NOT NULL,
  `arms` varchar(30) NOT NULL,
  `area` varchar(30) DEFAULT NULL,
  `post` varchar(40) NOT NULL,
  `city` varchar(15) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `pin` varchar(15) DEFAULT NULL,
  `icd` varchar(20) DEFAULT NULL,
  `ab64` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `officialdata`
--

INSERT INTO `officialdata` (`number`, `h_name`, `adno`, `rank`, `name`, `unitwaddress`, `service`, `station`, `command`, `nkin`, `relation`, `mobile`, `cdano`, `roffice`, `addroffice`, `totals`, `arms`, `area`, `post`, `city`, `state`, `pin`, `icd`, `ab64`) VALUES
('13993255-H', 'Military Hospital,Amritsar', '1', 'HAV', 'P.K SINGH', '90 ARMD,NAMS 56 APO', 'Army', 'AMRITSAR', 'WESTERN', 'RAHUL SINGH', 'SON', '9572753245', 'N/A', 'ARMD RECORDS', 'AHMEDABAD,99 APO', '10', 'GD', 'P-23/5,RED ENCLAVE,NAMS', 'KHASA', 'AMRITSAR', 'PUNJAB', '143107', 'N/A', 'N/A');

-- --------------------------------------------------------

--
-- Table structure for table `patientdata`
--

CREATE TABLE `patientdata` (
  `number` varchar(30) NOT NULL,
  `datetime` datetime NOT NULL,
  `dischargedate` datetime DEFAULT NULL,
  `adddate` date NOT NULL,
  `disdate` date DEFAULT NULL,
  `h_name` varchar(50) NOT NULL,
  `n_patient` varchar(50) NOT NULL,
  `r_patient` varchar(50) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `age` varchar(7) NOT NULL,
  `martial` varchar(10) NOT NULL,
  `religion` varchar(10) NOT NULL,
  `typead` varchar(50) DEFAULT NULL,
  `transfer` varchar(100) NOT NULL,
  `disease` varchar(200) DEFAULT NULL,
  `diet` varchar(50) DEFAULT NULL,
  `received` varchar(20) DEFAULT NULL,
  `diagnosis` varchar(200) DEFAULT NULL,
  `seenby` varchar(50) DEFAULT NULL,
  `ward` varchar(15) DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patientdata`
--

INSERT INTO `patientdata` (`number`, `datetime`, `dischargedate`, `adddate`, `disdate`, `h_name`, `n_patient`, `r_patient`, `sex`, `age`, `martial`, `religion`, `typead`, `transfer`, `disease`, `diet`, `received`, `diagnosis`, `seenby`, `ward`, `remarks`) VALUES
('13993255-H', '2019-01-14 15:00:00', '2019-01-14 15:10:09', '2019-01-14', '2019-01-14', 'Military Hospital,Amritsar', 'ANJALI SINGH', 'WIFE', 'Female', '27', 'Married', 'HINDU', 'Direct', 'N/A', 'SEVERE FEVER WITH BREATHING CONGESTION', 'NORMAL', 'Walking', 'N/A', 'CAPT ANU', 'F-3', 'N/A'),
('13993255-H', '2019-05-20 16:20:00', NULL, '2019-05-20', NULL, 'Military Hospital,Amritsar', 'ajit', 'bro', 'Male', '22', 'Married', 'hindu', 'Direct', 'N/A', 'n/a', 'n/a', 'Walking', 'N/A', 'n/a', 'n/a', 'N/A'),
('13993255-H', '2019-06-07 11:23:00', '2019-06-07 11:31:08', '2019-06-07', '2019-06-07', 'Military Hospital,Amritsar', 'rahul', 'bro', 'Male', '20', 'Single', 'hindu', 'Recat', 'N/A', 'na', 'normal', 'Sitting', 'N/A', 'hw', 'sd', 'N/A'),
('13993255-H', '2019-06-08 11:03:00', '2019-06-08 11:05:03', '2019-06-08', '2019-06-08', 'Military Hospital,Amritsar', 'rah', 'bro', 'Male', '15', 'Single', 'hindu', 'Reassessment Medical Board', 'N/A', 'any', 'normal', 'Sitting', 'N/A', 'na', 'na', 'N/A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `officialdata`
--
ALTER TABLE `officialdata`
  ADD PRIMARY KEY (`number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
