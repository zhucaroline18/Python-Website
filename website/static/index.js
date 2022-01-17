function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
    }).then((_res)=> {
        window.location.href = "/";
    });
}
//takes note id we pass and send post request to delete note endpoint
//after response, reload window and redirects to home page and refreshes page 