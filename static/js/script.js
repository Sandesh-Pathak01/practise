let isLiked = false;
let likeCount = 12; // Initial like count

function toggleLike() {
    isLiked = !isLiked;
    likeCount += isLiked ? 1 : -1;

    // Update the like count
    document.getElementById('likeCount').innerText = likeCount;

    // Change the color of the like button based on the like status
    const likeButton = document.querySelector('.like-button');
    likeButton.style.color = isLiked ? '#1877f2' : '';
}
