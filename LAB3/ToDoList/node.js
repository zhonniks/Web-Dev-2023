document.querySelector('#push').onclick = function(){
    if(document.querySelector('#newtask input').value.length == 0){
        alert("Enter Task Name!")
    }

    else{
        document.querySelector('#tasks').innerHTML += `
            <div class="task">

            <label>
            <input type = "checkbox" id = "myCheckBox" value 
            first_checkbox>
                <span id="taskname">
                ${document.querySelector('#newtask input').value}
                </span>
            </label>
                <button class="delete">
                    <i class="far fa-trash-alt"></i>
                    Delete
                </button>
            </div>
        `;

        var current_tasks = document.querySelectorAll(".delete");
        for(var i=0; i<current_tasks.length; i++){
            current_tasks[i].onclick = function(){
                this.parentNode.remove();
            }
            document.getElementById("my_input").value = "";
        }
        

        
    }
}
