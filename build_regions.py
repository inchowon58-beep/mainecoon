# -*- coding: utf-8 -*-
import os

regions = [
    {
        "slug": "incheon", "name": "인천", "keyword": "인천메인쿤분양", "area": "인천광역시",
        "hero": "IMG_6211.jpg", "about": "IMG_6185.jpg",
        "gallery": ["IMG_6188.jpg", "IMG_6197.jpg", "IMG_6202.jpg", "IMG_6095.jpg"],
        "nearby": "송도, 연수, 부평, 구월동, 청라",
        "intro": "인천 지역 가족을 위한 프리미엄 메인쿤분양 서비스입니다. 송도·연수·부평 등 인천 전역에서 상담과 방문 예약이 가능합니다.",
        "point1": "인천 거주 가족 맞춤 상담으로 라이프스타일에 맞는 메인쿤을 추천합니다.",
        "point2": "인천 인근 직접 방문 또는 화상 상담을 통해 메인쿤 고양이 종류와 성격을 확인할 수 있습니다.",
        "point3": "분양 후 인천 지역 그루밍·건강 관리 상담을 지속적으로 제공합니다.",
        "faq": "인천에서 메인쿤분양 상담은 전화(0505-464-1004)로 가능하며, 송도·부평·연수 등 인천 전 지역을 대상으로 합니다.",
    },
    {
        "slug": "bucheon", "name": "부천", "keyword": "부천메인쿤분양", "area": "부천시",
        "hero": "IMG_6097.jpg", "about": "IMG_6099.jpg",
        "gallery": ["IMG_133620E18487E185A9E186A8E18489E185A1.jpg", "IMG_133920E18487E185A9E186A8E18489E185A1.jpg", "IMG_134220E18487E185A9E186A8E18489E185A1.jpg", "IMG_134320E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "중동, 상동, 송내, 역곡",
        "intro": "부천시 및 인근 경기 서부 지역을 위한 메인쿤분양 전문 상담입니다. 아파트·단독주택 환경에 맞는 메인쿤 매칭을 도와드립니다.",
        "point1": "부천 지역 반려 가족을 위한 맞춤 메인쿤 성격 매칭 서비스를 제공합니다.",
        "point2": "부천 인근 방문 상담으로 새끼·성묘 메인쿤의 건강 상태를 직접 확인할 수 있습니다.",
        "point3": "메인쿤 크기와 털빠짐 관리법을 부천 생활 환경에 맞게 안내해 드립니다.",
        "faq": "부천메인쿤분양은 중동, 상동, 송내 등 부천 전역 상담이 가능합니다. 입양 문의 후 일정을 조율해 드립니다.",
    },
    {
        "slug": "siheung", "name": "시흥", "keyword": "시흥메인쿤분양", "area": "시흥시",
        "hero": "IMG_135520E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_135920E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_137220E18487E185A9E186A8E18489E185A1.jpg", "IMG_208520E18487E185A9E186A8E18489E185A1.jpg", "IMG_208620E18487E185A9E186A8E18489E185A1.jpg", "IMG_208720E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "정왕, 배곧, 월곶, 시흥능곡",
        "intro": "시흥시와 배곧 신도시 가족을 위한 메인쿤분양 안내입니다. 넓은 주거 공간에 어울리는 대형 메인쿤 분양을 전문으로 합니다.",
        "point1": "시흥·배곧 지역 대형 아파트에 적합한 메인쿤 크기와 성격 정보를 제공합니다.",
        "point2": "시흥 인근 방문 예약으로 실버 태비, 블루 스모크 등 다양한 메인쿤 고양이 종류를 소개합니다.",
        "point3": "분양 후 시흥 지역 사료·그루밍 관리 가이드를 맞춤 제공합니다.",
        "faq": "시흥메인쿤분양은 정왕, 배곧, 월곶 등 시흥 전역 상담 가능합니다. 배곧 신도시 가족 상담이 많습니다.",
    },
    {
        "slug": "gwangmyeong", "name": "광명", "keyword": "광명메인쿤분양", "area": "광명시",
        "hero": "IMG_209520E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_211720E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_212320E18487E185A9E186A8E18489E185A1.jpg", "IMG_212420E18487E185A9E186A8E18489E185A1.jpg", "IMG_212620E18487E185A9E186A8E18489E185A1.jpg", "IMG_212920E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "철산, 하안, 소하, 광명역",
        "intro": "광명시 및 서울 남서부 인근을 위한 프리미엄 메인쿤분양 서비스입니다. 광명·철산 지역 가족의 입양 상담을 전문적으로 진행합니다.",
        "point1": "광명 지역 통근 가족을 위한 독립심 강한 메인쿤 성격 매칭을 지원합니다.",
        "point2": "광명 인근 직접 방문으로 성묘·새끼 메인쿤 분양 상담이 가능합니다.",
        "point3": "메인쿤 털빠짐 시즌별 관리 팁을 광명 생활 환경에 맞게 안내합니다.",
        "faq": "광명메인쿤분양은 철산, 하안, 소하 등 광명시 전역과 인근 서울 지역 상담이 가능합니다.",
    },
    {
        "slug": "anyang", "name": "안양", "keyword": "안양메인쿤분양", "area": "안양시",
        "hero": "IMG_252220E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_252320E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_252920E18487E185A9E186A8E18489E185A1.jpg", "IMG_253420E18487E185A9E186A8E18489E185A1.jpg", "IMG_253620E18487E185A9E186A8E18489E185A1.jpg", "IMG_253720E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "평촌, 범계, 관양, 안양역",
        "intro": "안양시 평촌·범계 일대 가족을 위한 메인쿤분양 전문 페이지입니다. 안양 지역 반려인에게 최적화된 메인쿤 입양 상담을 제공합니다.",
        "point1": "안양 평촌·범계 지역 아파트 생활에 맞는 메인쿤 크기 안내를 제공합니다.",
        "point2": "안양 인근 방문 상담으로 메인쿤 고양이 종류별 특성을 비교할 수 있습니다.",
        "point3": "아이가 있는 안양 가족을 위한 온순한 메인쿤 성격 매칭을 전문으로 합니다.",
        "faq": "안양메인쿤분양은 평촌, 범계, 관양 등 안양시 전역 상담 가능합니다. 평촌 신도시 가족 문의가 많습니다.",
    },
    {
        "slug": "ansan", "name": "안산", "keyword": "안산메인쿤분양", "area": "안산시",
        "hero": "KakaoTalk_20260509_154040995.jpg", "about": "KakaoTalk_20260509_154040995_01.jpg",
        "gallery": ["KakaoTalk_20260509_154040995_02.jpg", "KakaoTalk_20260509_154040995_03.jpg", "KakaoTalk_20260509_154040995_04.jpg", "KakaoTalk_20260509_154040995_05.jpg"],
        "nearby": "단원, 상록, 고잔, 중앙역",
        "intro": "안산시 단원구·상록구 가족을 위한 메인쿤분양 안내입니다. 안산 지역에서 프리미엄 메인쿤 입양을 고려하시는 분들께 체계적인 상담을 제공합니다.",
        "point1": "안산 지역 대형 평수 주거에 적합한 메인쿤 크기·성격 정보를 안내합니다.",
        "point2": "안산 인근 방문으로 블루 스모크 등 프리미엄 메인쿤 고양이를 직접 만나볼 수 있습니다.",
        "point3": "분양 후 안산 지역 건강검진·예방접종 일정을 함께 관리해 드립니다.",
        "faq": "안산메인쿤분양은 단원구, 상록구, 고잔 등 안산 전역 상담이 가능합니다.",
    },
    {
        "slug": "ilsan", "name": "일산", "keyword": "일산메인쿤분양", "area": "고양시 일산",
        "hero": "KakaoTalk_20260509_154040995_06.jpg", "about": "KakaoTalk_20260509_154040995_07.jpg",
        "gallery": ["KakaoTalk_20260509_154040995_08.jpg", "KakaoTalk_20260509_154040995_09.jpg", "KakaoTalk_20260509_154040995_10.jpg", "KakaoTalk_20260509_154040995_11.jpg"],
        "nearby": "일산동구, 일산서구, 백석, 정발산",
        "intro": "일산신도시 및 고양시 일산 지역 가족을 위한 메인쿤분양 서비스입니다. 일산의 넓은 주거 환경에 어울리는 메인쿤 분양을 전문으로 합니다.",
        "point1": "일산 신도시 대형 아파트에 적합한 메인쿤 크기 가이드를 제공합니다.",
        "point2": "일산 인근 방문 상담으로 새끼·성묘 메인쿤의 성격을 직접 확인할 수 있습니다.",
        "point3": "일산 지역 메인쿤 털빠짐·그루밍 관리 노하우를 맞춤 안내합니다.",
        "faq": "일산메인쿤분양은 일산동구, 일산서구, 백석, 정발산 등 일산 전역 상담 가능합니다.",
    },
    {
        "slug": "gimpo", "name": "김포", "keyword": "김포메인쿤분양", "area": "김포시",
        "hero": "KakaoTalk_20260509_154040995_12.jpg", "about": "KakaoTalk_20260509_154040995_13.jpg",
        "gallery": ["KakaoTalk_20260509_154040995_14.jpg", "KakaoTalk_20260509_154040995_15.jpg", "KakaoTalk_20260509_154040995_16.jpg", "KakaoTalk_20260509_154040995_17.jpg"],
        "nearby": "구래, 장기, 김포한강, 운양",
        "intro": "김포시 및 한강 신도시 가족을 위한 프리미엄 메인쿤분양 안내입니다. 김포 지역 반려 가족에게 맞춤형 메인쿤 입양 상담을 제공합니다.",
        "point1": "김포 한강 신도시 넓은 주거 공간에 어울리는 대형 메인쿤 분양을 안내합니다.",
        "point2": "김포 인근 방문으로 메인쿤 고양이 종류와 건강 상태를 확인할 수 있습니다.",
        "point3": "김포 지역 가족을 위한 메인쿤 성격·크기 맞춤 추천 서비스를 운영합니다.",
        "faq": "김포메인쿤분양은 구래, 장기, 김포한강, 운양 등 김포시 전역 상담이 가능합니다.",
    },
    {
        "slug": "uijeongbu", "name": "의정부", "keyword": "의정부메인쿤분양", "area": "의정부시",
        "hero": "IMG_017320E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_019820E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_020620E18487E185A9E186A8E18489E185A1.jpg", "IMG_020820E18487E185A9E186A8E18489E185A1.jpg", "IMG_020920E18487E185A9E186A8E18489E185A1.jpg", "IMG_021020E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "의정부역, 가능, 호원, 민락",
        "intro": "의정부시 및 경기 북부 지역 가족을 위한 메인쿤분양 전문 상담입니다. 의정부·양주 인근에서 프리미엄 메인쿤 입양 상담을 진행합니다.",
        "point1": "의정부 지역 가족 맞춤 메인쿤 성격·크기 상담을 제공합니다.",
        "point2": "의정부 인근 방문으로 실버 태비 등 인기 메인쿤 고양이 종류를 소개합니다.",
        "point3": "경기 북부 지역 분양 후 건강·그루밍 관리 상담을 지속 제공합니다.",
        "faq": "의정부메인쿤분양은 의정부역, 가능, 호원, 민락 등 의정부시 전역 상담 가능합니다.",
    },
    {
        "slug": "gangnam", "name": "강남", "keyword": "강남메인쿤분양", "area": "서울 강남",
        "hero": "IMG_021220E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_023320E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_024320E18487E185A9E186A8E18489E185A1.jpg", "IMG_024520E18487E185A9E186A8E18489E185A1.jpg", "IMG_024620E18487E185A9E186A8E18489E185A1.jpg", "IMG_6095.jpg"],
        "nearby": "역삼, 삼성, 대치, 청담, 논현",
        "intro": "서울 강남권 프리미엄 가족을 위한 메인쿤분양 서비스입니다. 강남·서초·송파 인근에서 럭셔리 메인쿤 입양 상담을 전문적으로 제공합니다.",
        "point1": "강남 지역 프리미엄 라이프스타일에 맞는 메인쿤 고양이 종류를 추천합니다.",
        "point2": "강남 인근 프라이빗 상담으로 성묘·새끼 메인쿤 분양 일정을 조율합니다.",
        "point3": "강남 거주 가족을 위한 메인쿤 털빠짐·프리미엄 케어 관리 가이드를 제공합니다.",
        "faq": "강남메인쿤분양은 역삼, 삼성, 대치, 청담 등 강남권 전역 상담 가능합니다. 프리미엄 분양 상담을 전문으로 합니다.",
    },
    {
        "slug": "suwon", "name": "수원", "keyword": "수원메인쿤분양", "area": "수원시",
        "hero": "IMG_252220E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_252320E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_252920E18487E185A9E186A8E18489E185A1.jpg", "IMG_253420E18487E185A9E186A8E18489E185A1.jpg", "IMG_253620E18487E185A9E186A8E18489E185A1.jpg", "IMG_253720E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "영통, 팔달, 권선, 장안, 수원역",
        "intro": "수원시 및 경기 남부 지역 가족을 위한 메인쿤분양 전문 상담입니다. 영통·권선·장안 등 수원 전역에서 프리미엄 메인쿤 입양 상담을 진행합니다.",
        "point1": "수원 거주 가족의 주거 환경과 라이프스타일에 맞는 메인쿤 성격·크기 매칭을 제공합니다.",
        "point2": "수원 인근 방문 상담으로 새끼·성묘 메인쿤의 건강과 메인쿤 고양이 종류를 직접 확인할 수 있습니다.",
        "point3": "분양 후 수원 지역 그루밍·털빠짐 관리·건강 상담을 지속적으로 지원합니다.",
        "faq": "수원메인쿤분양은 영통, 팔달, 권선, 장안 등 수원시 전역 상담이 가능합니다.",
    },
    {
        "slug": "daegu", "name": "대구", "keyword": "대구메인쿤분양", "area": "대구광역시",
        "hero": "IMG_209520E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_211720E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_212320E18487E185A9E186A8E18489E185A1.jpg", "IMG_212420E18487E185A9E186A8E18489E185A1.jpg", "IMG_212620E18487E185A9E186A8E18489E185A1.jpg", "IMG_212920E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "수성구, 달서구, 북구, 동성로, 범어",
        "intro": "대구광역시 및 경북 인근 가족을 위한 프리미엄 메인쿤분양 서비스입니다. 수성·달서·범어 등 대구 전역에서 메인쿤 입양 상담이 가능합니다.",
        "point1": "대구 지역 가족 맞춤 메인쿤 크기·성격 상담으로 아파트·단독주택 환경에 맞는 분양을 안내합니다.",
        "point2": "대구 인근 방문 예약으로 실버 태비, 블루 스모크 등 인기 메인쿤 고양이 종류를 소개합니다.",
        "point3": "대구·경북 지역 분양 후 건강검진·예방접종·털 관리 상담을 제공합니다.",
        "faq": "대구메인쿤분양은 수성구, 달서구, 북구, 범어 등 대구 전역 상담이 가능합니다.",
    },
    {
        "slug": "busan", "name": "부산", "keyword": "부산메인쿤분양", "area": "부산광역시",
        "hero": "IMG_135520E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_135920E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_137220E18487E185A9E186A8E18489E185A1.jpg", "IMG_208520E18487E185A9E186A8E18489E185A1.jpg", "IMG_208620E18487E185A9E186A8E18489E185A1.jpg", "IMG_208720E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "해운대, 수영, 부산진, 남구, 센텀시티",
        "intro": "부산광역시 및 경남 인근 가족을 위한 메인쿤분양 전문 페이지입니다. 해운대·수영·부산진 등 부산 전역에서 프리미엄 메인쿤 입양 상담을 제공합니다.",
        "point1": "부산 해안 도시 생활에 맞는 메인쿤 크기·성격 정보와 실내 사육 가이드를 제공합니다.",
        "point2": "부산 인근 방문 상담으로 성묘·새끼 메인쿤의 품종 특성과 건강 상태를 확인할 수 있습니다.",
        "point3": "부산 지역 습도·환절기 털빠짐 관리법을 맞춤 안내해 드립니다.",
        "faq": "부산메인쿤분양은 해운대, 수영, 부산진, 남구 등 부산 전역 상담이 가능합니다.",
    },
    {
        "slug": "jeonju", "name": "전주", "keyword": "전주메인쿤분양", "area": "전주시",
        "hero": "IMG_6097.jpg", "about": "IMG_6099.jpg",
        "gallery": ["IMG_133620E18487E185A9E186A8E18489E185A1.jpg", "IMG_133920E18487E185A9E186A8E18489E185A1.jpg", "IMG_134220E18487E185A9E186A8E18489E185A1.jpg", "IMG_134320E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "완산구, 덕진구, 효자동, 전북대, 객사",
        "intro": "전주시 및 전북 지역 가족을 위한 메인쿤분양 안내입니다. 완산·덕진 등 전주 전역에서 체계적인 메인쿤 입양 상담을 진행합니다.",
        "point1": "전주 지역 가족의 생활 환경에 맞는 메인쿤 고양이 종류와 성격 매칭을 제공합니다.",
        "point2": "전주 인근 방문으로 메인쿤 크기·털빠짐 특성을 직접 확인하고 분양 일정을 조율할 수 있습니다.",
        "point3": "전주·전북 지역 분양 후 건강·그루밍 관리 상담을 지속 제공합니다.",
        "faq": "전주메인쿤분양은 완산구, 덕진구, 효자동 등 전주시 전역 상담이 가능합니다.",
    },
    {
        "slug": "ulsan", "name": "울산", "keyword": "울산메인쿤분양", "area": "울산광역시",
        "hero": "KakaoTalk_20260509_154040995.jpg", "about": "KakaoTalk_20260509_154040995_01.jpg",
        "gallery": ["KakaoTalk_20260509_154040995_02.jpg", "KakaoTalk_20260509_154040995_03.jpg", "KakaoTalk_20260509_154040995_04.jpg", "KakaoTalk_20260509_154040995_05.jpg"],
        "nearby": "남구, 중구, 울주, 삼산, 성남",
        "intro": "울산광역시 및 경남 동부 지역 가족을 위한 프리미엄 메인쿤분양 서비스입니다. 삼산·남구·울주 등 울산 전역 상담이 가능합니다.",
        "point1": "울산 지역 대형 주거 환경에 적합한 메인쿤 크기·성격 안내를 제공합니다.",
        "point2": "울산 인근 방문 상담으로 블루 스모크 등 프리미엄 메인쿤 분양 정보를 확인할 수 있습니다.",
        "point3": "분양 후 울산 지역 건강·사료·그루밍 관리 가이드를 맞춤 제공합니다.",
        "faq": "울산메인쿤분양은 남구, 중구, 울주, 삼산 등 울산 전역 상담이 가능합니다.",
    },
    {
        "slug": "mokpo", "name": "목포", "keyword": "목포메인쿤분양", "area": "목포시",
        "hero": "KakaoTalk_20260509_154040995_06.jpg", "about": "KakaoTalk_20260509_154040995_07.jpg",
        "gallery": ["KakaoTalk_20260509_154040995_08.jpg", "KakaoTalk_20260509_154040995_09.jpg", "KakaoTalk_20260509_154040995_10.jpg", "KakaoTalk_20260509_154040995_11.jpg"],
        "nearby": "상동, 하당, 북항, 평화광장, 목포역",
        "intro": "목포시 및 전남 서부 지역 가족을 위한 메인쿤분양 전문 상담입니다. 목포·무안 인근에서 프리미엄 메인쿤 입양 상담을 진행합니다.",
        "point1": "목포 지역 가족 맞춤 메인쿤 성격·크기 상담으로 반려 목적에 맞는 분양을 추천합니다.",
        "point2": "목포 인근 방문·화상 상담으로 메인쿤 고양이 종류와 분양 절차를 상세히 안내합니다.",
        "point3": "전남 서부 지역 분양 후 털빠짐·건강 관리 상담을 지속 제공합니다.",
        "faq": "목포메인쿤분양은 상동, 하당, 북항 등 목포시 전역 상담이 가능합니다.",
    },
    {
        "slug": "gwangju", "name": "광주", "keyword": "광주메인쿤분양", "area": "광주광역시",
        "hero": "KakaoTalk_20260509_154040995_12.jpg", "about": "KakaoTalk_20260509_154040995_13.jpg",
        "gallery": ["KakaoTalk_20260509_154040995_14.jpg", "KakaoTalk_20260509_154040995_15.jpg", "KakaoTalk_20260509_154040995_16.jpg", "KakaoTalk_20260509_154040995_17.jpg"],
        "nearby": "서구, 북구, 광산, 수완, 상무",
        "intro": "광주광역시 및 전남·전북 인근 가족을 위한 메인쿤분양 안내입니다. 수완·상무·광산 등 광주 전역에서 메인쿤 입양 상담이 가능합니다.",
        "point1": "광주 지역 아파트·주택 환경에 맞는 메인쿤 크기와 성격 정보를 제공합니다.",
        "point2": "광주 인근 방문 상담으로 성묘·새끼 메인쿤의 건강과 성격을 확인할 수 있습니다.",
        "point3": "광주 지역 환절기 털빠짐·그루밍 관리법을 맞춤 안내해 드립니다.",
        "faq": "광주메인쿤분양은 서구, 북구, 광산, 수완 등 광주 전역 상담이 가능합니다.",
    },
    {
        "slug": "daejeon", "name": "대전", "keyword": "대전메인쿤분양", "area": "대전광역시",
        "hero": "IMG_017320E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_019820E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_020620E18487E185A9E186A8E18489E185A1.jpg", "IMG_020820E18487E185A9E186A8E18489E185A1.jpg", "IMG_020920E18487E185A9E186A8E18489E185A1.jpg", "IMG_021020E18487E185A9E186A8E18489E185A1.jpg"],
        "nearby": "유성, 서구, 중구, 둔산, 대전역",
        "intro": "대전광역시 및 충청 지역 가족을 위한 프리미엄 메인쿤분양 서비스입니다. 유성·둔산·서구 등 대전 전역에서 입양 상담을 진행합니다.",
        "point1": "대전 지역 통근·가족 라이프스타일에 맞는 메인쿤 성격 매칭을 지원합니다.",
        "point2": "대전 인근 방문으로 메인쿤 고양이 종류별 특성과 분양 일정을 상담할 수 있습니다.",
        "point3": "분양 후 대전·충청 지역 건강·그루밍 관리 상담을 지속 제공합니다.",
        "faq": "대전메인쿤분양은 유성, 서구, 중구, 둔산 등 대전 전역 상담이 가능합니다.",
    },
    {
        "slug": "gimhae", "name": "김해", "keyword": "김해메인쿤분양", "area": "김해시",
        "hero": "IMG_021220E18487E185A9E186A8E18489E185A1.jpg", "about": "IMG_023320E18487E185A9E186A8E18489E185A1.jpg",
        "gallery": ["IMG_024320E18487E185A9E186A8E18489E185A1.jpg", "IMG_024520E18487E185A9E186A8E18489E185A1.jpg", "IMG_024620E18487E185A9E186A8E18489E185A1.jpg", "IMG_6095.jpg"],
        "nearby": "장유, 내외, 김해역, 대청, 삼안",
        "intro": "김해시 및 부산·창원 인근 가족을 위한 메인쿤분양 전문 상담입니다. 장유·내외·김해역 일대에서 프리미엄 메인쿤 입양 상담을 제공합니다.",
        "point1": "김해·장유 신도시 넓은 주거 환경에 어울리는 메인쿤 크기 가이드를 제공합니다.",
        "point2": "김해 인근 방문 상담으로 실버 태비 등 인기 메인쿤 고양이 종류를 소개합니다.",
        "point3": "경남 서부·부산 인근 분양 후 건강·털 관리 상담을 지속 지원합니다.",
        "faq": "김해메인쿤분양은 장유, 내외, 김해역, 대청 등 김해시 전역 상담이 가능합니다.",
    },
    {
        "slug": "jeju", "name": "제주도", "keyword": "제주도메인쿤분양", "area": "제주특별자치도",
        "hero": "IMG_6211.jpg", "about": "IMG_6185.jpg",
        "gallery": ["IMG_6188.jpg", "IMG_6197.jpg", "IMG_6202.jpg", "IMG_6095.jpg"],
        "nearby": "제주시, 서귀포, 애월, 표선, 중문",
        "intro": "제주특별자치도 거주 가족을 위한 메인쿤분양 전문 안내입니다. 제주시·서귀포 등 도내 전역에서 프리미엄 메인쿤 입양 상담을 진행합니다.",
        "point1": "제주도 독특한 기후와 실내 생활 환경에 맞는 메인쿤 크기·털 관리 정보를 제공합니다.",
        "point2": "제주 지역 방문·화상 상담으로 성묘·새끼 메인쿤 분양 일정을 조율할 수 있습니다.",
        "point3": "제주도 분양 후 건강검진·그루밍·사료 관리 상담을 지속 제공합니다.",
        "faq": "제주도메인쿤분양은 제주시, 서귀포, 애월, 중문 등 제주 전역 상담이 가능합니다.",
    },
]

out_dir = os.path.join(os.path.dirname(__file__), "pages", "regions")
os.makedirs(out_dir, exist_ok=True)

ASSET_VERSION = "20260619b"

REGIONAL_DROPDOWN_INLINE_CSS = """
  <style>
    .regional-links-dropdown{max-width:520px;margin:0 auto;border:1px solid #e0e0e0;background:#fff;box-shadow:0 4px 24px rgba(0,0,0,.06)}
    .regional-links-dropdown summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 22px;font-size:1.15rem;font-weight:500;color:#1a1a1a;user-select:none}
    .regional-links-dropdown summary::-webkit-details-marker{display:none}
    .regional-links-dropdown summary::marker{content:''}
    .regional-links-dropdown summary::after{content:'';flex-shrink:0;width:8px;height:8px;border-right:2px solid #c9a84c;border-bottom:2px solid #c9a84c;transform:rotate(45deg);margin-top:-4px}
    .regional-links-dropdown[open] summary{color:#c9a84c;border-bottom:1px solid #eee}
    .regional-links-dropdown[open] summary::after{transform:rotate(-135deg);margin-top:4px}
    .regional-links-dropdown:not([open]) .regional-links-panel{display:none}
    .regional-links-panel{max-height:280px;overflow-y:auto;-webkit-overflow-scrolling:touch}
    .regional-links-list a{display:block;padding:12px 22px;font-size:.88rem;font-weight:500;color:#888}
    .regional-links-list a:hover{color:#c9a84c;background:rgba(201,168,76,.06)}
    .regional-links-list li{border-bottom:1px solid #f0f0f0}
    .regional-links-list li:last-child{border-bottom:none}
  </style>"""

template = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{keyword} | {area} 프리미엄 메인쿤 고양이 분양 - 메인쿤분양 전문 캐터리</title>
  <meta name="description" content="{keyword} 전문 상담 — {area} {nearby} 인근 프리미엄 메인쿤 고양이 분양. 메인쿤 크기, 성격, 성묘·새끼 분양까지 {name} 지역 맞춤 안내.">
  <meta name="keywords" content="{keyword}, {name}메인쿤, {name}메인쿤입양, 메인쿤분양, 메인쿤고양이종류, 메인쿤크기, 메인쿤성격, 성묘, 털빠짐">
  <meta name="robots" content="index, follow">
  <meta name="naver-site-verification" content="df9aec9f2a5db9d8ef0eb68b0f8713b25a2b09fb" />
  <link rel="canonical" href="https://www.cattery.co.kr/pages/regions/{slug}.html">
  <meta property="og:title" content="{keyword} | {area} Maine Coon Cattery">
  <meta property="og:description" content="{area} {name} 지역 프리미엄 메인쿤분양 전문 상담">
  <meta property="og:image" content="https://www.cattery.co.kr/images/{hero}">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600&family=Noto+Sans+KR:wght@400;500&family=Noto+Serif+KR:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/style.css?v={asset_version}">
{regional_dropdown_css}
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"LocalBusiness","name":"{keyword} - 메인쿤분양 전문 캐터리","description":"{area} {name} 지역 프리미엄 메인쿤분양","url":"https://www.cattery.co.kr/pages/regions/{slug}.html","telephone":"0505-464-1004","areaServed":"{area}","image":"https://www.cattery.co.kr/images/{hero}","priceRange":"$$$$"}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"홈","item":"https://www.cattery.co.kr/"}},{{"@type":"ListItem","position":2,"name":"지역별 메인쿤분양","item":"https://www.cattery.co.kr/"}},{{"@type":"ListItem","position":3,"name":"{keyword}","item":"https://www.cattery.co.kr/pages/regions/{slug}.html"}}]}}
  </script>
</head>
<body>
  <header class="header">
    <div class="header-inner">
      <a href="../../index.html" class="logo"><span class="logo-ko">메인쿤분양 전문 캐터리</span><span class="logo-main">Maine Coon Cattery</span></a>
      <nav class="nav"><ul class="nav-list"><li><a href="../../index.html#about">Cattery</a></li><li><a href="../../index.html#services">Adoption</a></li><li><a href="../../index.html#gallery">Gallery</a></li><li><a href="../../index.html#contact">Contact</a></li></ul><button class="hamburger" aria-label="메뉴 열기"><span></span><span></span><span></span></button></nav>
    </div>
  </header>
  <nav class="mobile-nav" aria-label="모바일 메뉴"><button class="mobile-close" aria-label="메뉴 닫기">&times;</button><a href="../../index.html">Home</a><a href="../../index.html#contact">Contact</a></nav>

  <main>
    <section class="regional-hero">
      <div class="regional-hero-bg" style="background-image:url('../../images/{hero}')"></div>
      <div class="regional-hero-overlay"></div>
      <div class="container">
        <p class="breadcrumb" style="color:rgba(255,255,255,0.5);margin-bottom:16px;"><a href="../../index.html" style="color:var(--color-gold)">홈</a> &rsaquo; {keyword}</p>
        <p class="regional-en">{area} Premium Maine Coon</p>
        <h1>{keyword}</h1>
        <p class="regional-desc">{intro}</p>
        <div style="margin-top:32px;"><a href="tel:05054641004" class="btn btn-gold">{name} 입양문의</a></div>
      </div>
    </section>

    <section class="regional-about">
      <div class="regional-about-grid">
        <img src="../../images/{about}" alt="{keyword} 프리미엄 메인쿤" loading="lazy">
        <div>
          <h2>{area} 메인쿤분양 안내</h2>
          <p>{name} 지역({nearby} 등)에서 메인쿤분양을 찾고 계신다면, 메인쿤분양 전문 캐터리의 지역 맞춤 상담을 이용해 보세요. {name} 거주 가족의 생활 환경과 반려 목적에 맞는 메인쿤을 추천해 드립니다.</p>
          <p>메인쿤은 대형 장모종으로 메인쿤 크기, 메인쿤 성격, 털빠짐 관리 등 품종 특성을 미리 이해하는 것이 중요합니다. {keyword} 상담 시 메인쿤 고양이 종류별 특성과 분양 절차를 상세히 안내해 드립니다.</p>
          <p>{faq}</p>
        </div>
      </div>
    </section>

    <section class="regional-features">
      <h2>{name} 지역 {keyword} 특장점</h2>
      <div class="regional-features-grid">
        <div class="regional-feature-card"><h3>지역 맞춤 상담</h3><p>{point1}</p></div>
        <div class="regional-feature-card"><h3>방문·직접 확인</h3><p>{point2}</p></div>
        <div class="regional-feature-card"><h3>사후 관리 지원</h3><p>{point3}</p></div>
      </div>
    </section>

    <section class="regional-gallery">
      <h2>{name} {keyword} 갤러리</h2>
      <div class="regional-gallery-grid">
{gallery_html}
      </div>
    </section>

    <section class="article" style="padding-top:60px;padding-bottom:60px;">
      <div class="article-inner">
        <h2>{keyword} 자주 묻는 질문</h2>
        <p><strong>Q. {name}에서 메인쿤분양 상담이 가능한가요?</strong><br>A. 네, {faq}</p>
        <p><strong>Q. {name} 메인쿤분양 시 어떤 종류가 인기인가요?</strong><br>A. 실버 태비, 블루 스모크, 브라운 태비 등이 인기이며, {name} 가족 환경에 맞는 메인쿤 고양이 종류를 추천해 드립니다.</p>
        <p><strong>Q. {name}에서 성묘 분양도 가능한가요?</strong><br>A. 성묘 메인쿤 분양이 가능합니다. 성격이 안정된 성묘는 {name} 지역 초보 반려인에게도 적합합니다.</p>
        <div class="article-cta">
          <p>{keyword} 상담을 원하시면 지금 연락주세요.</p>
          <a href="tel:05054641004" class="btn btn-gold">{name} 메인쿤 입양문의 0505-464-1004</a>
        </div>
      </div>
    </section>

    <section class="regional-links">
      <div class="container">
        <details class="regional-links-dropdown">
          <summary>다른 지역 메인쿤분양</summary>
          <div class="regional-links-panel">
            <ul class="regional-links-list">
{related_html}
            </ul>
          </div>
        </details>
      </div>
    </section>
  </main>

  <footer class="footer"><div class="container"><div class="footer-bottom" style="border:none;"><p>&copy; MAINE COON CATTERY ALL RIGHTS RESERVED.</p><a href="../../index.html" class="btn-read" style="color:rgba(255,255,255,0.6);border-color:rgba(255,255,255,0.3);">홈으로</a></div></div></footer>
  <div class="fixed-bar">
    <a href="https://www.cattery.co.kr" target="_blank" rel="noopener"><span class="icon">&#127760;</span><span>캐터리 공식홈페이지</span><span class="en">www.cattery.co.kr</span></a>
    <a href="tel:05054641004" class="primary"><span class="icon">&#128222;</span><span>메인쿤 입양문의</span><span class="en">0505-464-1004</span></a>
  </div>
  <script src="../../js/main.js?v={asset_version}"></script>
</body>
</html>"""

for r in regions:
    gallery_html = "\n".join(
        f'        <img src="../../images/{img}" alt="{r["keyword"]} 메인쿤 고양이" loading="lazy">'
        for img in r["gallery"]
    )
    related_html = "\n".join(
        f'              <li><a href="{o["slug"]}.html">{o["keyword"]}</a></li>'
        for o in regions if o["slug"] != r["slug"]
    )
    html = template.format(
        gallery_html=gallery_html,
        related_html=related_html,
        asset_version=ASSET_VERSION,
        regional_dropdown_css=REGIONAL_DROPDOWN_INLINE_CSS,
        **r,
    )
    path = os.path.join(out_dir, f"{r['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {r['slug']}.html")

print(f"Done: {len(regions)} pages")
