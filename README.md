# Step With Dog (스위독)

![Step With Dog](https://user-images.githubusercontent.com/22683489/164723851-d454fd8e-e4d5-4139-8200-c4a0263a43d6.png)

**강아지와 함께 다니기 좋은 산책길을 공유할 수 있는 서비스**

강아지와 산책하기 좋은 곳을 누구든지 자유롭게 공유할 수 있습니다.<br/>
**추천** 탭을 통해 [서울 동물 복지지원 센터](https://animal.seoul.go.kr/animalplay)에서 스크랩핑한 내용을 제공합니다.

## 요구사항

### Python

의존성 패키지는 requirements.txt에 명시되어 있습니다.

``` bash
pip install -r requirements.txt
```

### 환경변수

``` bash
export MONGODB_HOST=”<HOST NAME>” 
export MONGODB_PORT=”<PORT NUMBER>” 
export MONGODB_USER=”<MONGODB USER>” 
export MONGODB_PASSWORD=”<MONGODB PASSWORD>”
```

## 사용법

``` bash
python app.py
```