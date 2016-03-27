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
