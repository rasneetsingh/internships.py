
SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

DROP TABLE IF EXISTS `internship`;
CREATE TABLE `internship` (
`CompanyName` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
`JobPosting` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
`RecruiterContact` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
`Sponsorship` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
`Apply` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
`Interview` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
`Offer` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,

#DumpingDataForTableInternship

Insert Into `internship` (`CompanyName`, `JobPosting`, `RecruiterContact`, `Sponsorship`,`Apply`,`Interview`,`Offer`) VALUES
('Google','STEP','Nathan','Yes','Yes','Yes','No'),
('Facebook','FBU','Sam','Yes','Yes','Yes','Yes'),
('Twitter','Twitter Academy','Jose','Yes','Yes','No','No'),
('Amazon','Propel Program','Brent','Yes','Yes','Yes','No'),
('Apple','SWE','Jonathan','Yes','Yes','Yes','Yes'),

ALTER TABLE `internship`
  ADD PRIMARY KEY (`CompanyName`);
