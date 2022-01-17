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
        console.log("Checked")
        node.parentNode.style.textDecoration  = "line-through";
    }
    else {
        node.parentNode.style.textDecoration  = "";
        console.log("Unchecked");
    }
}
//takes note id we pass and send post request to delete note endpoint
//after response, reload window and redirects to home page and refreshes page 