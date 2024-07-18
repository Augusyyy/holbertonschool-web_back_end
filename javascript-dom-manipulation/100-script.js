document.addEventListener("DOMContentLoaded", function() {
    // 获取所需的元素
    const addItem = document.getElementById("add_item");
    const removeItem = document.getElementById("remove_item");
    const clearList = document.getElementById("clear_list");
    const myList = document.querySelector(".my_list");

    // 添加新元素 <li>Item</li> 到列表
    addItem.addEventListener("click", function() {
        const newItem = document.createElement("li");
        newItem.textContent = "Item";
        myList.appendChild(newItem);
    });

    // 移除列表中的最后一个元素
    removeItem.addEventListener("click", function() {
        const lastItem = myList.lastElementChild;
        if (lastItem) {
            myList.removeChild(lastItem);
        }
    });

    // 清空列表中的所有元素
    clearList.addEventListener("click", function() {
        myList.innerHTML = "";
    });
});
