/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - project_track_assistant
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`project_track_assistant` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `project_track_assistant`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add coursetable',7,'add_coursetable'),
(26,'Can change coursetable',7,'change_coursetable'),
(27,'Can delete coursetable',7,'delete_coursetable'),
(28,'Can view coursetable',7,'view_coursetable'),
(29,'Can add datasettable',8,'add_datasettable'),
(30,'Can change datasettable',8,'change_datasettable'),
(31,'Can delete datasettable',8,'delete_datasettable'),
(32,'Can view datasettable',8,'view_datasettable'),
(33,'Can add logintable',9,'add_logintable'),
(34,'Can change logintable',9,'change_logintable'),
(35,'Can delete logintable',9,'delete_logintable'),
(36,'Can view logintable',9,'view_logintable'),
(37,'Can add studenttable',10,'add_studenttable'),
(38,'Can change studenttable',10,'change_studenttable'),
(39,'Can delete studenttable',10,'delete_studenttable'),
(40,'Can view studenttable',10,'view_studenttable'),
(41,'Can add topicstable',11,'add_topicstable'),
(42,'Can change topicstable',11,'change_topicstable'),
(43,'Can delete topicstable',11,'delete_topicstable'),
(44,'Can view topicstable',11,'view_topicstable'),
(45,'Can add stafftable',12,'add_stafftable'),
(46,'Can change stafftable',12,'change_stafftable'),
(47,'Can delete stafftable',12,'delete_stafftable'),
(48,'Can view stafftable',12,'view_stafftable'),
(49,'Can add projectnotificationstable',13,'add_projectnotificationstable'),
(50,'Can change projectnotificationstable',13,'change_projectnotificationstable'),
(51,'Can delete projectnotificationstable',13,'delete_projectnotificationstable'),
(52,'Can view projectnotificationstable',13,'view_projectnotificationstable'),
(53,'Can add intrestingareastable',14,'add_intrestingareastable'),
(54,'Can change intrestingareastable',14,'change_intrestingareastable'),
(55,'Can delete intrestingareastable',14,'delete_intrestingareastable'),
(56,'Can view intrestingareastable',14,'view_intrestingareastable'),
(57,'Can add feedbacktable',15,'add_feedbacktable'),
(58,'Can change feedbacktable',15,'change_feedbacktable'),
(59,'Can delete feedbacktable',15,'delete_feedbacktable'),
(60,'Can view feedbacktable',15,'view_feedbacktable'),
(61,'Can add complainttable',16,'add_complainttable'),
(62,'Can change complainttable',16,'change_complainttable'),
(63,'Can delete complainttable',16,'delete_complainttable'),
(64,'Can view complainttable',16,'view_complainttable'),
(65,'Can add chattable',17,'add_chattable'),
(66,'Can change chattable',17,'change_chattable'),
(67,'Can delete chattable',17,'delete_chattable'),
(68,'Can view chattable',17,'view_chattable');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(17,'project_assistant','chattable'),
(16,'project_assistant','complainttable'),
(7,'project_assistant','coursetable'),
(8,'project_assistant','datasettable'),
(15,'project_assistant','feedbacktable'),
(14,'project_assistant','intrestingareastable'),
(9,'project_assistant','logintable'),
(13,'project_assistant','projectnotificationstable'),
(12,'project_assistant','stafftable'),
(10,'project_assistant','studenttable'),
(11,'project_assistant','topicstable'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-02-22 05:15:49.259907'),
(2,'auth','0001_initial','2024-02-22 05:15:49.768990'),
(3,'admin','0001_initial','2024-02-22 05:15:49.872461'),
(4,'admin','0002_logentry_remove_auto_add','2024-02-22 05:15:49.884455'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-02-22 05:15:49.894723'),
(6,'contenttypes','0002_remove_content_type_name','2024-02-22 05:15:49.961319'),
(7,'auth','0002_alter_permission_name_max_length','2024-02-22 05:15:50.007374'),
(8,'auth','0003_alter_user_email_max_length','2024-02-22 05:15:50.059546'),
(9,'auth','0004_alter_user_username_opts','2024-02-22 05:15:50.074476'),
(10,'auth','0005_alter_user_last_login_null','2024-02-22 05:15:50.121452'),
(11,'auth','0006_require_contenttypes_0002','2024-02-22 05:15:50.125444'),
(12,'auth','0007_alter_validators_add_error_messages','2024-02-22 05:15:50.138694'),
(13,'auth','0008_alter_user_username_max_length','2024-02-22 05:15:50.186971'),
(14,'auth','0009_alter_user_last_name_max_length','2024-02-22 05:15:50.236826'),
(15,'auth','0010_alter_group_name_max_length','2024-02-22 05:15:50.263786'),
(16,'auth','0011_update_proxy_permissions','2024-02-22 05:15:50.280794'),
(17,'auth','0012_alter_user_first_name_max_length','2024-02-22 05:15:50.328774'),
(18,'project_assistant','0001_initial','2024-02-22 05:15:51.007372'),
(19,'sessions','0001_initial','2024-02-22 05:15:51.040626'),
(20,'project_assistant','0002_auto_20240222_1112','2024-02-22 05:42:58.147586'),
(21,'project_assistant','0003_auto_20240222_1229','2024-02-22 07:00:01.394300');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('zqg6hgsqr1wyv1fhoeo40lv5btc1bblf','.eJyrVkrOTFGyMtFRygHRRjpK2VB-Eog21FEqANO1AOwtCyg:1rl4In:4NI4irKwd-6g9Wtr5RnkfDEHF-1clA7nnldZmUeuUJw','2024-03-29 09:56:37.474345');

/*Table structure for table `project_assistant_chattable` */

DROP TABLE IF EXISTS `project_assistant_chattable`;

CREATE TABLE `project_assistant_chattable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `FROMID_id` bigint NOT NULL,
  `TOID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_assistant_ch_FROMID_id_7ddaea05_fk_project_a` (`FROMID_id`),
  KEY `project_assistant_ch_TOID_id_a6e48744_fk_project_a` (`TOID_id`),
  CONSTRAINT `project_assistant_ch_FROMID_id_7ddaea05_fk_project_a` FOREIGN KEY (`FROMID_id`) REFERENCES `project_assistant_logintable` (`id`),
  CONSTRAINT `project_assistant_ch_TOID_id_a6e48744_fk_project_a` FOREIGN KEY (`TOID_id`) REFERENCES `project_assistant_logintable` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_chattable` */

/*Table structure for table `project_assistant_complainttable` */

DROP TABLE IF EXISTS `project_assistant_complainttable`;

CREATE TABLE `project_assistant_complainttable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(500) NOT NULL,
  `reply` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_assistant_co_STUDENT_id_245310b9_fk_project_a` (`STUDENT_id`),
  CONSTRAINT `project_assistant_co_STUDENT_id_245310b9_fk_project_a` FOREIGN KEY (`STUDENT_id`) REFERENCES `project_assistant_studenttable` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_complainttable` */

insert  into `project_assistant_complainttable`(`id`,`complaint`,`reply`,`date`,`STUDENT_id`) values 
(5,'hvvju,k','jh','2024-03-01',4);

/*Table structure for table `project_assistant_coursetable` */

DROP TABLE IF EXISTS `project_assistant_coursetable`;

CREATE TABLE `project_assistant_coursetable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `course` varchar(50) NOT NULL,
  `details` varchar(200) NOT NULL,
  `noofsem` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_coursetable` */

insert  into `project_assistant_coursetable`(`id`,`course`,`details`,`noofsem`) values 
(1,'MCA','2 Years Post Gratuation','8'),
(3,'BBA','dfghjk','6');

/*Table structure for table `project_assistant_datasettable` */

DROP TABLE IF EXISTS `project_assistant_datasettable`;

CREATE TABLE `project_assistant_datasettable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `area` varchar(50) NOT NULL,
  `keywords` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=164 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_datasettable` */

insert  into `project_assistant_datasettable`(`id`,`area`,`keywords`) values 
(1,'cn','network'),
(2,'cn','network pro'),
(3,'cn','TCP/IP'),
(4,'cn','LAN'),
(5,'cn','WAN'),
(6,'cn','Ethernet'),
(7,'cn','Wi-Fi'),
(8,'cn','Router'),
(9,'cn','Switch'),
(10,'cn','Firewall'),
(11,'cn','VPN'),
(12,'cn','DNS'),
(13,'cn','IPv4/IPv6'),
(14,'cn','Subnet'),
(15,'cn','DHCP'),
(16,'cn','NAT'),
(17,'cn','FTP'),
(18,'cn','HTTP/HTTPS'),
(19,'cn','VoIP'),
(20,'cn','Cloud Computing'),
(21,'cn','IoT'),
(22,'cn','Packet'),
(23,'cn','Bandwidth'),
(24,'cn','Latency'),
(25,'cn','QoS'),
(26,'cn','TCP congestion control'),
(27,'cn','Load Balancing'),
(28,'ai','Machine Learning (ML)'),
(29,'ai','Deep Learning'),
(30,'ai','Neural Networks'),
(31,'ai','Natural Language Processing (NLP)'),
(32,'ai','Computer Vision'),
(33,'ai','Reinforcement Learning'),
(34,'ai','Generative Adversarial Networks (GANs)'),
(35,'ai','Transfer Learning'),
(36,'ai','AI Ethics'),
(37,'ai','Explainable AI (XAI)'),
(38,'ai','AI Interpretability'),
(39,'ai','AI Governance'),
(40,'ai','AI Safety'),
(41,'ai','Knowledge Representation and Reasoning'),
(42,'ai','AI Planning'),
(43,'ai','Cognitive Computing'),
(44,'ai','AI Applications'),
(45,'ai','AI Robotics'),
(46,'ai','AI Assistants'),
(47,'ai','AI Hardware'),
(48,'ml','Supervised Learning'),
(49,'ml','machine learning'),
(50,'ml','Unsupervised Learning'),
(51,'ml','Semi-Supervised Learning'),
(52,'ml','Reinforcement Learning'),
(53,'ml','Deep Learning'),
(54,'ml','Neural Networks'),
(55,'ml','Convolutional Neural Networks (CNNs)'),
(56,'ml','Recurrent Neural Networks (RNNs)'),
(57,'ml','Transfer Learning'),
(58,'ml','Feature Engineering'),
(59,'ml','Dimensionality Reduction'),
(60,'ml','Ensemble Learning'),
(61,'ml','Cross-Validation'),
(62,'ml','Hyperparameter Tuning'),
(63,'ml','Loss Function'),
(64,'ml','Gradient Descent'),
(65,'ml','Overfitting and Underfitting'),
(66,'ml','Bias-Variance Tradeoff'),
(67,'ml','Regularization'),
(68,'ml','Model Evaluation Metrics'),
(69,'dl','Neural Networks'),
(70,'dl','Deep Neural Networks (DNNs)'),
(71,'dl','deep learnng'),
(72,'dl','Artificial Neurons'),
(73,'dl','Feedforward Neural Networks'),
(74,'dl','Backpropagation'),
(75,'dl','Activation Functions'),
(76,'dl','Convolutional Neural Networks (CNNs)'),
(77,'dl','Recurrent Neural Networks (RNNs)'),
(78,'dl','Long Short-Term Memory (LSTM)'),
(79,'dl','Gated Recurrent Units (GRUs)'),
(80,'dl','Autoencoders:'),
(81,'dl','Generative Adversarial Networks (GANs)'),
(82,'dl','Deep Reinforcement Learning'),
(83,'dl','Transfer Learning'),
(84,'dl','Attention Mechanism'),
(85,'dl','Deep Learning Frameworks'),
(86,'dl','Data Augmentation'),
(87,'dl','Hyperparameter Optimization'),
(88,'dl','Model Interpretability'),
(89,'dl','Deep Learning Applications'),
(90,'bc','Cryptocurrency'),
(91,'bc','Bitcoin'),
(92,'bc','Ethereum'),
(93,'bc','Altcoins'),
(94,'bc','Stablecoins'),
(95,'bc','Tokenomics'),
(96,'bc','Decentralized Finance (DeFi)'),
(97,'bc','Blockchain Technology:'),
(98,'bc','Distributed Ledger Technology (DLT)'),
(99,'bc','Smart Contracts'),
(100,'bc','Consensus Mechanisms'),
(101,'bc','Mining'),
(102,'bc','Proof of Work (PoW)'),
(103,'bc','Proof of Stake (PoS)'),
(104,'bc','Byzantine Fault Tolerance (BFT)'),
(105,'bc','Forks (Hard fork, Soft fork)'),
(106,'bc','Healthcare'),
(107,'bc','Supply Chain Management'),
(108,'bc','Voting Systems'),
(109,'bc','Identity Verification'),
(110,'bc','Intellectual Property Rights'),
(111,'bc','Real Estate'),
(112,'bc','Gaming and Collectibles'),
(113,'bc','Enterprise Blockchain'),
(114,'bc','Hyperledger'),
(115,'bc','Corda'),
(116,'bc','Enterprise Ethereum Alliance (EEA)'),
(118,'bc','Permissioned Blockchains'),
(119,'bc','Private Blockchains'),
(120,'bc','Interoperability'),
(121,'bc','Sharding'),
(122,'bc','Cryptocurrency Regulations'),
(123,'bc','Know Your Customer (KYC)'),
(124,'bc','Anti-Money Laundering (AML)'),
(125,'bc','Securities and Exchange Commission (SEC)'),
(126,'bc','General Data Protection Regulation (GDPR)'),
(127,'bc','Blockchain Development'),
(128,'bc','Solidity (for Ethereum smart contracts)'),
(129,'bc','Web3.js'),
(130,'bc','Truffle Suite'),
(131,'bc','Ethereum Virtual Machine (EVM)'),
(132,'bc','IPFS (InterPlanetary File System)'),
(133,'bc','Layer 2 Solutions (e.g., Lightning Network)'),
(134,'bc','Sidechains'),
(135,'bc','Raiden Network (for Ethereum)'),
(136,'bc','Tokenization'),
(137,'bc','Initial Coin Offerings (ICOs)'),
(138,'bc','Security Token Offerings (STOs)'),
(139,'bc','Non-Fungible Tokens (NFTs)'),
(140,'bc','Token Standards (e.g., ERC-20, ERC-721)'),
(141,'bc','Decentralized Autonomous Organizations (DAOs)'),
(142,'bc','Central Bank Digital Currencies (CBDCs)'),
(143,'bc','Web3.0'),
(144,'bc','Quantum Blockchain'),
(145,'bc','Metaverse'),
(146,'nlp','Tokenization'),
(147,'nlp','Text Classification'),
(148,'nlp','Named Entity Recognition (NER)'),
(149,'nlp','Part-of-Speech Tagging (POS)'),
(150,'nlp','Sentiment Analysis'),
(151,'nlp','Topic Modeling'),
(152,'nlp','Word Embeddings'),
(153,'nlp','Dependency Parsing'),
(154,'nlp','Language Modeling'),
(155,'nlp','Machine Translation'),
(156,'nlp','Question Answering'),
(157,'nlp','Text Generation'),
(158,'nlp','Text Summarization'),
(159,'nlp','Dialogue Systems (Chatbots)'),
(160,'nlp','Cross-lingual NLP'),
(161,'nlp','Pretrained Models'),
(162,'nlp','Attention Mechanisms'),
(163,'nlp','Zero-shot Learning');

/*Table structure for table `project_assistant_feedbacktable` */

DROP TABLE IF EXISTS `project_assistant_feedbacktable`;

CREATE TABLE `project_assistant_feedbacktable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_assistant_fe_STUDENT_id_8a4d22ff_fk_project_a` (`STUDENT_id`),
  CONSTRAINT `project_assistant_fe_STUDENT_id_8a4d22ff_fk_project_a` FOREIGN KEY (`STUDENT_id`) REFERENCES `project_assistant_studenttable` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_feedbacktable` */

/*Table structure for table `project_assistant_intrestingareastable` */

DROP TABLE IF EXISTS `project_assistant_intrestingareastable`;

CREATE TABLE `project_assistant_intrestingareastable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `details` varchar(200) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_assistant_in_STAFF_id_a15ea806_fk_project_a` (`STAFF_id`),
  CONSTRAINT `project_assistant_in_STAFF_id_a15ea806_fk_project_a` FOREIGN KEY (`STAFF_id`) REFERENCES `project_assistant_stafftable` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_intrestingareastable` */

insert  into `project_assistant_intrestingareastable`(`id`,`details`,`STAFF_id`) values 
(3,'ai',1),
(5,'ml',1),
(7,'nlp',4),
(8,'bc',3);

/*Table structure for table `project_assistant_logintable` */

DROP TABLE IF EXISTS `project_assistant_logintable`;

CREATE TABLE `project_assistant_logintable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_logintable` */

insert  into `project_assistant_logintable`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'staff','staff','staff'),
(5,'chjklgty','','admin'),
(6,'chjklgty','','admin'),
(9,'abc','123','student'),
(10,'abc','123','student'),
(11,'abc','123','staff'),
(12,'staff1','staff1','staff');

/*Table structure for table `project_assistant_projectnotificationstable` */

DROP TABLE IF EXISTS `project_assistant_projectnotificationstable`;

CREATE TABLE `project_assistant_projectnotificationstable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `details` varchar(200) NOT NULL,
  `year` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `lastdate` date NOT NULL,
  `COURSE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_assistant_pr_COURSE_id_04cf4b2a_fk_project_a` (`COURSE_id`),
  CONSTRAINT `project_assistant_pr_COURSE_id_04cf4b2a_fk_project_a` FOREIGN KEY (`COURSE_id`) REFERENCES `project_assistant_coursetable` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_projectnotificationstable` */

insert  into `project_assistant_projectnotificationstable`(`id`,`details`,`year`,`date`,`lastdate`,`COURSE_id`) values 
(1,'submit your first review mainproject','2025','2024-02-22','2024-02-29',3),
(2,'submit your second review mainproject ','2024','2024-02-22','2024-03-01',1),
(3,'submit your last review','2024','2024-02-22','2024-03-02',1),
(6,'submit today your topic','2024','2024-02-14','2024-02-29',1);

/*Table structure for table `project_assistant_stafftable` */

DROP TABLE IF EXISTS `project_assistant_stafftable`;

CREATE TABLE `project_assistant_stafftable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `Phoneno` bigint NOT NULL,
  `email` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `qualification` varchar(200) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_assistant_st_LOGIN_id_1358298d_fk_project_a` (`LOGIN_id`),
  CONSTRAINT `project_assistant_st_LOGIN_id_1358298d_fk_project_a` FOREIGN KEY (`LOGIN_id`) REFERENCES `project_assistant_logintable` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_stafftable` */

insert  into `project_assistant_stafftable`(`id`,`fname`,`lname`,`Phoneno`,`email`,`image`,`qualification`,`LOGIN_id`) values 
(1,'anu','p',987654567,'anup12@gmail.com','girl3.jpg','MCA',2),
(3,'balu','Kp',9365214811,'balukk123@gmail.com','boy4.webp','PHD in computer application',11),
(4,'Farhana','P',9747098703,'farhananoushad1212@gmail.com','imageLAM.jpg','MCA',12);

/*Table structure for table `project_assistant_studenttable` */

DROP TABLE IF EXISTS `project_assistant_studenttable`;

CREATE TABLE `project_assistant_studenttable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `RegisterNo` int NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `semester` int NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` int NOT NULL,
  `Phoneno` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `COURSE_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_assistant_st_COURSE_id_1b8822aa_fk_project_a` (`COURSE_id`),
  KEY `project_assistant_st_LOGIN_id_de052b67_fk_project_a` (`LOGIN_id`),
  CONSTRAINT `project_assistant_st_COURSE_id_1b8822aa_fk_project_a` FOREIGN KEY (`COURSE_id`) REFERENCES `project_assistant_coursetable` (`id`),
  CONSTRAINT `project_assistant_st_LOGIN_id_de052b67_fk_project_a` FOREIGN KEY (`LOGIN_id`) REFERENCES `project_assistant_logintable` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_studenttable` */

insert  into `project_assistant_studenttable`(`id`,`RegisterNo`,`fname`,`lname`,`semester`,`dob`,`gender`,`place`,`post`,`pin`,`Phoneno`,`email`,`year`,`image`,`COURSE_id`,`LOGIN_id`) values 
(4,17465,'Farhana','P',4,'2024-02-04','female','tirur','niramaruthur',676109,9747098703,'farhananoushad1212@gmail.com','2024','girl2.png',3,10);

/*Table structure for table `project_assistant_topicstable` */

DROP TABLE IF EXISTS `project_assistant_topicstable`;

CREATE TABLE `project_assistant_topicstable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `heading` varchar(50) NOT NULL,
  `file` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `staff_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_assistant_to_STUDENT_id_8bf1286e_fk_project_a` (`STUDENT_id`),
  KEY `project_assistant_topicstable_staff_id_de0b9dc4` (`staff_id`),
  CONSTRAINT `project_assistant_to_staff_id_de0b9dc4_fk_project_a` FOREIGN KEY (`staff_id`) REFERENCES `project_assistant_stafftable` (`id`),
  CONSTRAINT `project_assistant_to_STUDENT_id_8bf1286e_fk_project_a` FOREIGN KEY (`STUDENT_id`) REFERENCES `project_assistant_studenttable` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project_assistant_topicstable` */

insert  into `project_assistant_topicstable`(`id`,`heading`,`file`,`date`,`status`,`staff_id`,`STUDENT_id`) values 
(4,'mm','nn','2024-03-01','accepted',1,4),
(5,'recipe','nn','2024-03-27','rejected',3,4);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
