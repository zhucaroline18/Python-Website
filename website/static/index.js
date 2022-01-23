function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
    }).then((_res)=> {
        window.location.href = "/";
    });
}


function strikethrough(node) {
    if (node.checked) {
        //console.log("Checked")
        node.parentNode.style.textDecoration  = "line-through";
    }
    else {
        node.parentNode.style.textDecoration  = "";
        //console.log("Unchecked");
    }
}

function dateChanged(node, noteId) {
    console.log("dateChanged to " + node.value);

    fetch('/set-deadline', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId, date: node.value })
    }).then((_res)=> {
        window.location.href = "/";
    });

}


//takes note id we pass and send post request to delete note endpoint
//after response, reload window and redirects to home page and refreshes page 