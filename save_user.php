<?php
// user.csv 파일 경로
define("CSV_FILE", "user.csv");

// POST 요청 처리
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST["username"];
    $password = password_hash($_POST["password"], PASSWORD_BCRYPT); // 비밀번호 암호화
    $gender = $_POST["gender"];
    $age = $_POST["age"];
    $animalTestLink = $_POST["animalTestLink"];
    $animalTestResult = $_POST["animalTestResult"];
    $discTestLink = $_POST["discTestLink"];
    $discTestResult = $_POST["discTestResult"];

    // CSV에 저장할 데이터 배열
    $userData = [
        $username,
        $password,
        $gender,
        $age,
        $animalTestLink,
        $animalTestResult,
        $discTestLink,
        $discTestResult
    ];

    // user.csv 파일 생성 및 헤더 추가
    if (!file_exists(CSV_FILE)) {
        $header = [
            "아이디", "비밀번호", "성별", "나이",
            "동물상 테스트 링크", "동물상 테스트 결과",
            "DISC 검사 링크", "DISC 검사 결과"
        ];
        $file = fopen(CSV_FILE, "w");
        fputcsv($file, $header);
        fclose($file);
    }

    // CSV에 사용자 데이터 추가
    $file = fopen(CSV_FILE, "a");
    fputcsv($file, $userData);
    fclose($file);

    // 성공 응답
    echo json_encode(["success" => true, "message" => "회원가입이 완료되었습니다."]);
    exit();
}
?>
