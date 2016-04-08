/**
 * Created by timandrews on 3/25/16.
 */

//DatePicker Fields
$( "#reminderStartDate" ).datepicker();
$( "#displayDate" ).datepicker();
$( "#plantingDate" ).datepicker();


//Change following button to un-follow on hover
$(".btnFollowing").hover(
    function() {
        var $this = $(this); // caching $(this)
        $this.data('Following', $this.text());
        $this.text('un-Follow');
        $this.removeClass('btn-success');
        $this.addClass('btn-warning')
    },
    function() {
        var $this = $(this); // caching $(this)
        $this.text($this.data('Following'));
        $this.removeClass('btn-warning');
        $this.addClass('btn-success')
    }
);


// toggleFollowing: remove following
$('.btnFollowing').on('click', function() {
    //alert(this.id);
    $.getJSON('/toggleFollowing', {
        id: this.id },
        function(results) {
            //alert(results.button_id);
            $("#" + results.button_id).removeClass('btnFollowing btn-success btn-warning ');
            $("#" + results.button_id).text('Follow');
            $("#" + results.button_id).addClass('btn-default btnNotFollowing');
            // unbind hover event.  keep un-hover from happinging
            $("#" + results.button_id).unbind('mouseenter mouseleave')
        }
    );
});

// toggleNotFollowing: add following
$('.btnNotFollowing').on('click', function() {
    //alert(this.id);
    $.getJSON('/toggleNotFollowing', {
        id: this.id },
        function(results) {
            //alert(results.button_id);
            $('#' + results.button_id).text('Following');
            $('#' + results.button_id).removeClass('btn-default btnNotFollowing');
            $('#' + results.button_id).addClass('btn-success btnFollowing');
            // rebind hover event.  
            $("#" + results.button_id).bind('mouseenter mouseleave')
        }
    );
});
