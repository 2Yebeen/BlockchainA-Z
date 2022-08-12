# 블록체인 만들기

[블록체인_정리](https://velog.io/@33bini/series/Blockchain-A-Z)

## 데모 확인

작업 폴더에서 코드를 실행시키는 것이 권장 사항이므로 코드를 실행하기 전 파일 탐색 창에서 알맞은 폴더로 이동하는 것을 추천합니다.

1. 코드를 전체 선택 후 실행 시켜줍니다.(F9)

2. `get_chain`요청을 먼저 확인해 봅니다.
<img width="650" src="https://velog.velcdn.com/images/33bini/post/d7a70023-0467-4071-96f2-5d6a3e70983c/image.png">
- 하나의 제네시스 블록만 있는 블록체인이 생성되었습니다. 
- 이전 해시는 `0`이고 증명은 `1`입니다.

3. `mine_block`요청에서 블록을 채굴해 봅니다.
<img width="650" src="https://velog.velcdn.com/images/33bini/post/ee23fb22-30d3-468e-b050-13bbe1ca74a8/image.png">
- 이전 해시는 제네시스 블록에서 만든 해시 함수로 확인해 볼 수 있습니다.
- 블록을 채굴하기는 꽤 쉽습니다. 문제의 복잡성을 높이고 싶다면 작업을 복잡하게 만들어야 합니다.

4. 블록을 여러개 만들고, 길이와 정보가 제대로 입력되는지 확인 합니다.
<img width="650" src="https://velog.velcdn.com/images/33bini/post/62e1ae4b-1546-4155-bdec-a54c416c6c87/image.png">

5. 유효한 블록체인인지 확인 해봅니다.
<img width="650" src="https://user-images.githubusercontent.com/68188768/184290536-0dd872a4-7195-4480-b6cb-2ce3c1670d45.png">
