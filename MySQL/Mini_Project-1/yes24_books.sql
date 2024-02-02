-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: yes24
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `bookID` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `publishing` date DEFAULT NULL,
  `rating` decimal(3,1) DEFAULT NULL,
  `review` int DEFAULT NULL,
  `sales` int DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `ranking` int DEFAULT NULL,
  `ranking_weeks` int DEFAULT NULL,
  PRIMARY KEY (`bookID`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'마흔에 읽는 쇼펜하우어','강용수 저','유노북스','2023-09-07',9.0,277,897429,17000.00,1,9),(2,'나는 메트로폴리탄 미술관의 경비원입니다','패트릭 브링리 저/김희정, 조현주 역','웅진지식하우스','2023-11-24',9.5,550,420540,17500.00,2,5),(3,'세이노의 가르침','세이노(SayNo) 저','데이원','2023-03-02',9.0,1959,2165169,7200.00,3,22),(4,'ETS 토익 정기시험 기출문제집 1000 Vol. 4 RC','ETS 저','YBM(와이비엠)','2023-12-20',9.8,32,294741,19800.00,4,6),(5,'ETS 토익 정기시험 기출문제집 1000 Vol. 4 LC','ETS 저','YBM(와이비엠)','2023-12-20',9.7,26,276681,19800.00,5,6),(6,'퓨처 셀프','벤저민 하디 저/최은아 역','상상스퀘어','2023-08-30',8.7,330,633630,19800.00,6,2),(7,'이처럼 사소한 것들','클레어 키건 저/홍한별 역','다산책방','2023-11-27',9.6,106,208944,13800.00,7,3),(8,'남에게 보여주려고 인생을 낭비하지 마라','아르투어 쇼펜하우어 저/박제헌 역','페이지2','2023-10-30',9.3,99,322683,17500.00,8,12),(9,'아이는 무엇으로 자라는가','버지니아 사티어 저/강유리 역','포레스트북스','2023-12-18',9.8,8,84888,17500.00,9,1),(10,'처음부터 시작하는 주식투자 단타전략','홍인기 저','길벗','2023-12-22',8.5,98,332697,21000.00,10,4),(11,'도둑맞은 집중력','요한 하리 저/김하현 역','어크로스','2023-04-28',8.8,627,593976,18800.00,11,36),(12,'푸바오, 언제나 사랑해','에버랜드 동물원 글그림/강철원 글/류정훈 사진','시공주니어','2024-01-25',10.0,68,209436,23000.00,13,1),(13,'유목민의 투자의 정석','유목민 저','리더스북','2024-01-17',9.8,41,150318,28000.00,14,3),(14,'2024 큰별쌤 최태성의 별별한국사 기출 500제 한국사능력검정시험 심화 (1,2,3급)','최태성 저','이투스북','2024-01-17',10.0,2,106941,19500.00,15,1),(15,'당신의 인생이 왜 힘들지 않아야 한다고 생각하십니까','아르투어 쇼펜하우어 저/김욱 역','포레스트북스','2023-06-21',9.4,205,310164,17500.00,16,9),(16,'2024~2025 대한민국 산업지도','이래학 저','경이로움','2024-01-17',9.7,12,62853,27000.00,17,1),(17,'생각이 너무 많은 어른들을 위한 심리학 (10만부 돌파 기념 스페셜 에디션)','김혜남 저','메이븐','2023-09-25',9.6,113,240093,17800.00,18,8),(18,'최소한의 한국사','최태성 저','프런트페이지','2023-06-21',9.8,341,383295,18000.00,19,25),(19,'아홉 살에 시작하는 똑똑한 초등신문','신효원 저','책장속북스','2023-05-05',9.8,292,317574,17500.00,20,8),(20,'2024 큰별쌤 최태성의 별별한국사 한국사능력검정시험 심화(1,2,3급) 하','최태성 저','이투스북','2023-12-01',10.0,14,267900,15500.00,21,5),(21,'퍼스널 MBA','조시 카우프만 저/박상진, 이상호 역','진성북스','2024-01-25',10.0,3,51537,35500.00,22,1),(22,'트렌드 코리아 2024','김난도, 전미영, 최지혜, 이수진, 권정윤 저 외 6명 정보 더 보기/감추기','미래의창','2023-10-05',9.3,356,583785,19000.00,23,3),(23,'2024 큰별쌤 최태성의 별별한국사 한국사능력검정시험 심화(1,2,3급) 상','최태성 저','이투스북','2023-12-01',9.9,18,276351,16000.00,24,5),(24,'데일 카네기 인간관계론 (무삭제 완역본)','데일 카네기 저/임상훈 역','현대지성','2019-10-07',9.6,940,297426,11500.00,25,10),(25,'하와이 대저택 100일 미라클','하와이 대저택 저','메가스터디북스','2024-01-25',5.4,19,71259,19800.00,26,1),(26,'역행자 확장판','자청 저','웅진지식하우스','2023-05-29',8.8,427,456927,19500.00,27,26),(27,'읽으면서 바로 써먹는 어린이 세계 여행','한날 글그림','파란정원','2024-01-05',9.7,24,85788,13000.00,28,4),(28,'느리게 나이 드는 습관','정희원 저','한빛라이프','2023-12-11',9.8,39,127899,18000.00,29,9),(29,'AI 2024','김덕진 저','스마트북스','2023-10-25',9.7,42,135801,22000.00,30,10),(30,'사랑인 줄 알았는데 부정맥','사단법인 전국유료실버타운협회, 포푸라샤 편집부 저/이지수 역','포레스트북스','2024-01-17',9.6,50,71157,13300.00,31,2),(31,'그 속에서 놀던 때가 그립습니다','택리지 저','테라코타','2024-01-01',10.0,3,48693,18000.00,32,0),(32,'맡겨진 소녀','클레어 키건 저/허진 역','다산책방','2023-04-26',9.6,461,119646,13000.00,33,4),(33,'빨간내복야코 2','빨간내복야코 원저/서후 글그림','샌드박스스토리 키즈','2024-01-24',0.0,0,38607,15000.00,34,1),(34,'해커스 토익 기출 VOCA 보카','David Cho 저','해커스어학연구소','2023-07-24',9.5,890,356445,12900.00,35,63),(35,'모순','양귀자 저','쓰다','2013-04-01',9.6,843,218313,13000.00,36,38),(36,'비트코인 슈퍼 사이클','신민철(처리형) 저','거인의정원','2024-01-25',8.7,12,31683,25000.00,37,1),(37,'SQL 자격검정 실전문제','한국데이터진흥원 저','한국데이터산업진흥원','2023-12-29',0.0,0,49755,18000.00,38,1),(38,'내가 한 말을 내가 오해하지 않기로 함','문상훈 저','위너스북','2024-01-05',9.5,139,284286,19800.00,39,1),(39,'ETS 토익기출 파트별 VOCA 보카','ETS 저','YBM(와이비엠)','2022-12-23',9.7,91,224790,13000.00,40,17),(40,'나에게 들려주는 예쁜 말','김종원 글/나래 그림','상상아이','2024-02-01',10.0,11,44334,16800.00,41,1),(41,'이은경쌤의 초등어휘일력 365','이은경 저','포레스트북스','2022-10-28',9.8,261,286782,18800.00,42,15),(42,'요즘 어른을 위한 최소한의 세계사','임소미 저/김봉중 감수','빅피시','2023-09-22',9.7,133,241914,18800.00,43,12),(43,'뇌, 욕망의 비밀을 풀다','한스-게오르크 호이젤 저/강영옥, 김신종, 한윤진 역','비즈니스북스','2019-10-04',9.2,178,80010,18000.00,44,4),(44,'죽음이 물었다, 어떻게 살 거냐고','한스 할터 저/한윤진 역','포레스트북스','2023-12-25',9.1,56,110805,17800.00,45,1),(45,'원씽 THE ONE THING','게리 켈러, 제이 파파산 저/구세희 역','비즈니스북스','2013-08-30',9.4,734,364866,16800.00,46,36),(46,'우리가 작별 인사를 할 때마다','마거릿 렌클 저/최정수 역','을유문화사','2023-12-25',9.7,23,27102,17000.00,47,1),(47,'내가 생각한 인생이 아니야','류시화 저','수오서재','2023-12-21',9.7,65,130170,18000.00,48,2),(48,'돈의 속성 300쇄 리커버','김승호 저','스노우폭스북스','2020-06-15',9.4,1569,337143,17800.00,49,42),(49,'그리스 로마 신화 37','박시연 글/최우빈 그림/김헌 감수','아울북','2024-01-24',10.0,18,32238,15000.00,50,1),(50,'내가 원하는 곳에 나를 데려가라','네빌 고다드 저/김은영 역','터닝페이지','2024-01-31',9.1,9,20313,19000.00,51,1),(51,'좋은 일이 오려고 그러나 보다 (리커버판)','박여름 저','히읏','2023-07-26',9.4,48,167481,16800.00,52,23),(52,'ETS 토익 단기공략 750+ (LC+RC)','ETS 저','YBM(와이비엠)','2020-08-20',9.7,210,186324,18000.00,53,12),(53,'아주 희미한 빛으로도','최은영 저','문학동네','2023-08-07',9.7,282,203199,16800.00,54,6),(54,'구의 증명','최진영 저','은행나무','2023-04-26',9.2,113,162753,12000.00,55,32),(55,'밥 프록터의 본 리치','밥 프록터 저/김문주 역','비즈니스북스','2024-01-19',9.8,81,30582,16800.00,56,1),(56,'흔한남매 15','흔한남매 원저/백난도 글/유난희 그림/흔한컴퍼니 감수','미래엔아이세움','2023-12-14',9.8,142,187878,14500.00,57,5),(57,'용선생 교과서 세계사 1','사회평론 역사연구소, 송용운, 김언진, 길병민, 한승준 글 외 5명 정보 더 보기/감추기','사회평론','2023-12-18',10.0,83,73908,16000.00,58,4),(58,'성공하는 리더들의 영어 필사 100일의 기적','퍼포먼스 코치 제이, 퍼포먼스 코치 리아 저','넥서스','2023-11-25',9.9,50,64212,17000.00,59,2),(59,'2024.2025 큰별쌤 최태성의 별별한국사 시대별 기출문제집 한국사능력검정시험 심화(1,2,3급)','최태성 저','이투스북','2023-12-26',10.0,8,97575,19500.00,60,4),(60,'황금종이 1','조정래 저','해냄','2023-11-21',9.5,112,189756,18500.00,61,5),(61,'나는 주식으로 월급 두 번 받는다','공돌투자자 저','알에이치코리아(RHK)','2024-01-30',10.0,2,22236,22000.00,62,1),(62,'황금종이 2','조정래 저','해냄','2023-11-21',9.4,50,176874,18500.00,63,5),(63,'지옥 초등학교 1','아리타 나오 글/안라쿠 마사시 그림/이소담 역','한빛에듀','2024-01-08',10.0,69,46824,14500.00,64,3),(64,'흔한남매 과학 탐험대 0 과학의 기초','흔한남매 원저/김언정, 이현진 글/김덕영 그림/최진수 감수 외 4명 정보 더 보기/감추기','주니어김영사','2023-12-27',9.8,41,91875,14800.00,65,5),(66,'결국 해내는 사람들의 원칙 (리커버 에디션)','바바라 피즈, 앨런 피즈 저/이재경 역','반니','2020-12-14',9.6,45,116916,18000.00,67,12),(67,'부의 추월차선 (10주년 스페셜 에디션)','엠제이 드마코 저/신소영 역','토트출판사','2022-02-04',8.9,1131,189075,17500.00,68,71),(68,'원피스 ONE PIECE 107','오다 에이이치로 글그림','대원','2024-01-15',9.6,48,70677,5500.00,69,4),(69,'메리골드 마음 사진관','윤정은 저','북로망스','2024-01-12',9.9,77,51048,17000.00,70,2),(70,'사는 동안 한 번은 팔아봐라','서과장 저','마인드셋(Mindset)','2024-01-10',9.3,17,57858,19800.00,71,2),(71,'나는 배당투자로 매일 스타벅스 커피를 공짜로 마신다','송민섭(수페TV) 저','21세기북스','2023-12-06',9.8,72,141243,24000.00,72,2),(72,'10대를 위한 총균쇠 수업','김정진 저','넥스트씨','2023-08-15',9.8,59,117447,16000.00,73,10);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-02 23:36:48
