<div align="center">
<h1>🐢자율 이동 터틀봇</h1>
</div>

## 목차
  - [개요](#개요) 
  - [프로젝트 목표](#프로젝트-목표)
  - [구동 방식](#구동-방식)

## 개요
- 프로젝트 개발기간: 2024.03.07-2024.03.8
- 개발 툴 및 언어: Ros2 & Raspberry pi4 & turtlebot & ubuntu & python
- 멤버: 송인태

## 프로젝트 목표 
- Ros2 수업기간은 단 1주일이었다. 터틀봇과 네트워크 연결하는데도 꼬박 3일이 걸렸다. 나머지 2틀동안 나름 의미 있는 미니 프로젝트를 생각하던 중 터틀봇으로 원하는 위치까지 움직이는 나만의 미니 프로젝트를 진행해 보기로 했다.

## 구동 방식

### 하드웨어 연결 💻<br>

터틀봇에 장착되어 있는 라즈베리파이와 제어할 PC를 Wi-Fi Hotspot 으로 연결한다.이때 nmap 네트워크 스캔후 ssh 라즈베리 파이 연결이 핵심이다.<br>
```py
$ nmap -sn 10.42.0.0/24
```
```py
$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}
```
![image](https://github.com/dlsxo1023/Turtlebot_miniproject/assets/149138829/057b413c-8e98-48b7-b71a-cc6e09e44247)

### SLAM Node 맵 만들기 🗺️<br>
1. bringup실행
```py
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
```
2. 새 터미널 창에서 SLAM Cartographer 실행
```py
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_cartographer cartographer.launch.py
```
3. SLAM Noderk 성공적으로 실행되면 텔레오퍼레이션으로 미지역 탐색
```py
$ export TURTLEBOT3_MODEL=burger
$ ros2 run turtlebot3_teleop teleop_keyboard

Control Your TurtleBot3!
---------------------------
Moving around:
       w
  a    s    d
       x

w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
space key, s : force stop

CTRL-C to quit
```

4. 이렇게 완성시 map 관련 pgm파일 , yaml파일이 생성된다
![image](https://github.com/dlsxo1023/Turtlebot_miniproject/assets/149138829/24878796-b401-4c35-b31a-d61453342709)

### Navigation Nodes 실행🚗

1. navigation2 실행
```py
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/map.yaml
```

![image](https://github.com/dlsxo1023/Turtlebot_miniproject/assets/149138829/b36f9483-91a9-457d-9308-de1f6c462ae0)

![image](https://github.com/dlsxo1023/Turtlebot_miniproject/assets/149138829/1ab22e8c-3c4c-44a2-8b48-de53d30cc2c7)

2. publish , subscribe 실행<br>
pub_nav_msg.py / sub_n_follow.py 코드는 아래 참조<br>
[코드보기](https://github.com/dlsxo1023/Turtlebot_miniproject/tree/master/nav_pkg/nav_pkg)

### 터틀봇 이동 방법

|이동방향|1번 좌표|2번 좌표|3번 좌표|4번 좌표|
|---|---|---|---|---|
|키보드| 1 | 2 | 3 | 4 |

### 구연 영상

|Navi|Turtlebot|
|---|---|
|![KakaoTalk_20240327_053236652](https://github.com/dlsxo1023/Turtlebot_miniproject/assets/149138829/af0b01c0-53eb-4f62-8f8e-e4e4665a635e)|![KakaoTalk_20240327_053238430](https://github.com/dlsxo1023/Turtlebot_miniproject/assets/149138829/f9395326-4fb8-415f-b3ab-1252882b383a)|
