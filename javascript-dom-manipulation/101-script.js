document.addEventListener("DOMContentLoaded", function() {
    // 获取所需的元素
    const translateButton = document.getElementById("btn_translate");
    const languageCodeSelect = document.getElementById("language_code");
    const helloDiv = document.getElementById("hello");

    // 监听按钮点击事件
    translateButton.addEventListener("click", function() {
        const languageCode = languageCodeSelect.value;

        // 确保选择了语言代码
        if (languageCode) {
            // 构建API URL
            const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

            // 发送请求获取翻译
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    // 显示翻译结果
                    helloDiv.textContent = data.hello;
                })
                .catch(error => {
                    console.error('Error fetching translation:', error);
                    helloDiv.textContent = "Error fetching translation";
                });
        } else {
            helloDiv.textContent = "Please select a language code";
        }
    });
});
