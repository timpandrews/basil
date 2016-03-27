/**
 * Created by timandrews on 3/25/16.
 */


//Change following button to un-follow on hover
$('.btnFollowing').hover(
    function() {
        var $this = $(this); // caching $(this)
        $this.data('Following', $this.text());
        $this.text('un-Follow');
        $this.removeClass('btn-success')
        $this.addClass('btn-warning')
    },
    function() {
        var $this = $(this); // caching $(this)
        $this.text($this.data('Following'));
        $this.removeClass('btn-warning')
        $this.addClass('btn-success')
    }
);


// toggleFollowing: remove following
$('.btnFollowing').on('click', function() {
    alert(this.id);
    $.getJSON('/toggleFollowing', {
        id: this.id },
        function(results) {

            alert(results.returnValue);
        }
    );
});

// toggleNotFollowing: add following
$('.btnNotFollowing').on('click', function() {
    alert(this.id);
    $.getJSON('/toggleNotFollowing', {
        id: this.id },
        function(results) {
            
            alert(results.returnValue);

        }
    );
});
