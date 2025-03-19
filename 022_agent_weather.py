import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """도시의 현재 날씨 정보를 웹 스크레이핑을 통해 반환합니다.
    
    Args:
        city (str): 날씨를 조회할 도시 이름 (영어로 입력, 예: Seoul)
        
    Returns:
        str: 도시의 현재 날씨 정보
        
    Raises:
        Exception: 웹 페이지 로드 또는 파싱 실패 시
    """
    url = f"https://www.timeanddate.com/weather/south-korea/{city.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        temp = soup.find("div", class_="h2")  # 온도 정보
        if temp:
            weather_info = temp.get_text(strip=True)
            return f"{city}의 현재 날씨 정보: {weather_info}"
        else:
            return f"{city}의 날씨 정보를 찾을 수 없습니다."
    except requests.RequestException as e:
        return f"{city}의 날씨 정보를 가져오는 데 실패했습니다: {str(e)}"
    except Exception as e:
        return f"오류 발생: {str(e)}"

# 테스트
if __name__ == "__main__":
    # 도구를 직접 호출하는 대신 invoke 사용
    result = get_weather.invoke({"city": "Seoul"})
    print(result)