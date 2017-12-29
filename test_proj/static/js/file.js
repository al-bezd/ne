function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function Success(data, textStatus, jqXHR){
  $('body').html(jqXHR.responseText);
  location.reload();
  }
function Active(b){
	console.log(b.id);

	$('.blog-nav-item').removeClass('active');
	//$(b).addClass('active');
}
function ToFollow(id){
	$.ajax({
          type:"POST",
          url:"to_follow",
	          data:{
	          	'id':id,
	            'csrfmiddlewaretoken':getCookie('csrftoken'),
	          },
	      dataType:'html',
          success:Success });}


function DelFollow(id){
	$.ajax({
          type:"POST",
          url:"del_follow",
	          data:{
	          	'id':id,
	            'csrfmiddlewaretoken':getCookie('csrftoken'),
	          },
          success:Success,
          dataType:'html'
          });
}

function AddRead(id){
	$.ajax({
          type:"POST",
          url:"add_read",
	          data:{
	          	'id':id,
	            'csrfmiddlewaretoken':getCookie('csrftoken'),
	          },
          success:Success,
          dataType:'html'
          });
}
