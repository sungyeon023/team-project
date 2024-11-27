<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>회원가입 및 로그인</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
        }
        .container {
            max-width: 500px;
            margin: auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        label {
            display: block;
            margin-top: 10px;
            font-weight: bold;
        }
        input, select, textarea {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            margin-top: 15px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .link {
            display: block;
            text-align: center;
            margin-top: 10px;
            color: #007BFF;
            cursor: pointer;
        }
        .link:hover {
            text-decoration: underline;
        }
        .info {
            margin-top: 20px;
            background: #f9f9f9;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <!-- 로그인 페이지 -->
    <div id="login-container" class="container">
        <h1>로그인</h1>
        <form id="login-form">
            <label for="login-username">아이디</label>
            <input type="text" id="login-username" required>

            <label for="login-password">비밀번호</label>
            <input type="password" id="login-password" required>

            <button type="submit">로그인</button>
            <p class="link" id="to-signup">회원가입 페이지로 이동</p>
        </form>
    </div>

    <!-- 회원가입 페이지 -->
    <div id="signup-container" class="container" style="display:none;">
        <h1>회원가입</h1>
        <form id="signup-form">
            <label for="username">아이디</label>
            <input type="text" id="username" required>

            <label for="password">비밀번호</label>
            <input type="password" id="password" required>

            <label for="gender">성별</label>
            <select id="gender" required>
                <option value="">선택</option>
                <option value="male">남성</option>
                <option value="female">여성</option>
                <option value="other">기타</option>
            </select>

            <label for="age">나이</label>
            <input type="number" id="age" required>

            <label for="animal-test-link">얼굴상(동물상) 테스트 링크</label>
            <input type="url" id="animal-test-link" placeholder="https://example.com">

            <label for="animal-test-result">테스트 결과</label>
            <textarea id="animal-test-result" rows="3" placeholder="결과를 입력하세요"></textarea>

            <label for="disc-test-link">DISC 검사 링크</label>
            <input type="url" id="disc-test-link" placeholder="https://example.com (번역기능 포함)">

            <label for="disc-test-result">DISC 검사 결과</label>
            <textarea id="disc-test-result" rows="3" placeholder="결과를 입력하세요"></textarea>

            <button type="submit">회원가입</button>
        </form>
    </div>

    <!-- 프로필 페이지 -->
    <div id="profile-container" class="container" style="display:none;">
        <h1>내 정보</h1>
        <div id="user-info" class="info"></div>
        <button id="logout">로그아웃</button>
    </div>

    <script>
        // HTML 요소 참조
        const signupContainer = document.getElementById('signup-container');
        const loginContainer = document.getElementById('login-container');
        const profileContainer = document.getElementById('profile-container');
        const signupForm = document.getElementById('signup-form');
        const loginForm = document.getElementById('login-form');
        const userInfo = document.getElementById('user-info');
        const toSignup = document.getElementById('to-signup');
        const logoutButton = document.getElementById('logout');

        // 회원가입 페이지로 이동
        toSignup.addEventListener('click', function() {
            loginContainer.style.display = 'none';
            signupContainer.style.display = 'block';
        });

        // 회원가입 데이터 저장
        signupForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const user = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                gender: document.getElementById('gender').value,
                age: document.getElementById('age').value,
                animalTestLink: document.getElementById('animal-test-link').value,
                animalTestResult: document.getElementById('animal-test-result').value,
                discTestLink: document.getElementById('disc-test-link').value,
                discTestResult: document.getElementById('disc-test-result').value
            };

            localStorage.setItem(user.username, JSON.stringify(user));
            alert('회원가입이 완료되었습니다!');
            signupForm.reset();
            signupContainer.style.display = 'none';
            loginContainer.style.display = 'block';
        });

        // 로그인 처리
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const username = document.getElementById('login-username').value;
            const password = document.getElementById('login-password').value;

            const storedUser = JSON.parse(localStorage.getItem(username));

            if (storedUser && storedUser.password === password) {
                alert('로그인 성공!');
                displayUserInfo(storedUser);
            } else {
                alert('아이디 또는 비밀번호가 잘못되었습니다.');
            }
        });

        // 사용자 정보 표시
        function displayUserInfo(user) {
            userInfo.innerHTML = `
                <p><strong>아이디:</strong> ${user.username}</p>
                <p><strong>성별:</strong> ${user.gender}</p>
                <p><strong>나이:</strong> ${user.age}</p>
                <p><strong>동물상 테스트 링크:</strong> <a href="${user.animalTestLink}" target="_blank">${user.animalTestLink}</a></p>
                <p><strong>동물상 테스트 결과:</strong> ${user.animalTestResult}</p>
                <p><strong>DISC 검사 링크:</strong> <a href="${user.discTestLink}" target="_blank">${user.discTestLink}</a></p>
                <p><strong>DISC 검사 결과:</strong> ${user.discTestResult}</p>
            `;
            loginContainer.style.display = 'none';
            profileContainer.style.display = 'block';
        }

        // 로그아웃 처리
        logoutButton.addEventListener('click', function() {
            profileContainer.style.display = 'none';
            loginContainer.style.display = 'block';
            loginForm.reset();
        });
    </script>
</body>
</html>
