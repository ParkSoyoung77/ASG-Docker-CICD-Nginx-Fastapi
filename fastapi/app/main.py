from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# --- [ 서비스 페이지 영역 ] ---

# A. 게시판 페이지
@app.get("/board", response_class=HTMLResponse)
async def get_board():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>[CI/CD]의 AWS 게시판</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; text-align: center; background: #f8f9fa; padding: 20px; }
        nav { background: #333; padding: 10px; margin-bottom: 20px; border-radius: 10px; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
        .container { max-width: 900px; margin: auto; background: white; padding: 25px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        th { background: #009639; color: white; }
        .write-box { background: #eee; padding: 20px; border-radius: 10px; margin-top: 30px; text-align: left; }
        .btn { background: #009639; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; width: 100%; font-weight: bold; }
    </style>
</head>
<body>
    <nav>
        <a href="/">메인</a>
        <a href="/company">회사소개</a>
        <a href="/board">게시판</a>
        <a href="/guestbook">방명록</a>
    </nav>
    <div class="container">
        <h1>[CI/CD]의 실시간 AWS 게시판</h1>
        <div id="board-list"><p>게시글 목록 로딩 기능은 DB 연결 해제로 인해 비활성화되었습니다.</p></div>
        <div class="write-box">
            <h3>비회원 글쓰기 (실습용)</h3>
            <input type="text" id="author" placeholder="작성자 이름">
            <input type="password" id="pw" placeholder="비밀번호">
            <input type="text" id="title" placeholder="제목">
            <textarea id="content" rows="4" placeholder="내용을 입력하세요" style="width:98%"></textarea>
            <button class="btn" onclick="writePost()">게시글 등록 (작동 안함)</button>
        </div>
    </div>
    <script>
        function writePost() {
            alert('현재 DB 연결이 없어 게시글을 등록할 수 없습니다.');
        }
    </script>
</body>
</html>
    """

# B. 방명록 페이지
@app.get("/guestbook", response_class=HTMLResponse)
async def get_guestbook():
    return """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>[CI/CD]의 AWS 방명록</title>
<style>
    body { font-family: 'Segoe UI', sans-serif; text-align: center; background: #fff5e6; padding: 20px; }
    nav { background: #333; padding: 10px; margin-bottom: 20px; border-radius: 10px; }
    nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
    .container { max-width: 700px; margin: auto; background: white; padding: 25px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    .input-area { background: #eee; padding: 20px; border-radius: 10px; margin-top: 20px; text-align: left; }
    .btn-orange { background: #e67e22; color: white; border: none; padding: 12px; width: 100%; border-radius: 5px; cursor: pointer; font-weight: bold; }
</style>
</head>
<body>
    <nav>
        <a href="/">메인</a> 
        <a href="/company">회사소개</a> 
        <a href="/board">게시판</a> 
        <a href="/guestbook">방명록</a>
    </nav>
    <div class="container">
        <h1>[CI/CD]의 실시간 방명록</h1>
        <div id="guest-list"><p>방명록 데이터가 없습니다. (DB 연결 해제)</p></div>
        <div class="input-area">
            <h3>방명록 남기기</h3>
            <input type="text" id="g-name" placeholder="작성자">
            <textarea id="g-msg" rows="3" placeholder="메시지를 입력하세요" style="width:98%"></textarea>
            <button class="btn-orange" onclick="writeGuest()">방명록 등록 (작동 안함)</button>
        </div>
    </div>
    <script>
        function writeGuest() {
            alert('현재 DB 연결이 없어 방명록을 등록할 수 없습니다.');
        }
    </script>
</body>
</html>
    """

# --- [ API 데이터 처리 영역 ] ---
@app.post("/api/write")
async def write_post():
    return {"status": "error", "message": "Database not connected"}

@app.get("/api/list")
async def list_posts():
    return []

@app.get("/api/guest-list")
async def list_guests():
    return []