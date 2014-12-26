$(document).ready(function(){
    console.log("ready");
        
    $('#check_update').hide();
    $('#check_reset').hide();
    var last_content = "";

    $('#search').on('click', function() 
      {  
	chemical = $('#chemical').val();
	if (chemical == "")
	  { 
	    alert("Please do not leave this field blank")
	  }
	
	$.ajax({
	    type: "GET",
	    url: "/mol_2_chemfig/_get_smiles",
	    data : { 'chemical': chemical},
	    success: function(data)
	    {
	    $('#txt_area').val(data.smiles);          
		if  ($("#txt_area").val() == "\n")
		  {
		    alert("Sorry, the name you requested was not found in the database." + "\n" + "Please check spelling or use ChemDoodle scketcher to generate MOL format.")
		  }
	    },
	    error: function(error) 
	    {
		console.log(error)
	    }
	});
	
      });

    $('#convert').on('click', function(){
	$( "input[value='-w']" ).prop('checked', true);
	if ($("#txt_area").val() == "")
	  {
	    alert("Please do not leave this field blank")  
	  }
	function get_check_value() {
	    var p=[];		
	    $('input[name="check"]:checked').each(function () {
		p.push(this.value);
	    });	
	    return p.join(',');
	}
	smiles_mol = $("#txt_area").val();
	hydrogens = $('#H2 :selected').text();
	
	if (smiles_mol.indexOf("%") == -1){	   
            last_content = smiles_mol;
	    angle = $('input[name="angle"]').val();		
	    $.ajax ({
		type: "GET",
		url: "/mol_2_chemfig/smiles_to_chemfig",
		data: {"smiles_mol": smiles_mol, "check": get_check_value(), "angle": angle, 'hydrogens': hydrogens},			    
		success: function(data2){
		    if (data2.pdf_link == 'Chemfig cannot be generated')
			{
			  alert("Oops.. Chemfig cannot be generated. Please check the structure for errors (e.g. a 5-valence carbon)");
			}
		    else{
			   $("#txt_area").val(data2.chem_fig);	
			    $("#pdf").attr('src', data2.pdf_link);
			    $('#check_update').show();
			    $('#check_reset').show();
		        }
		       },
		    error: function(Error) {
			console.log(error)
		    }
		     })
	} else{
	    alert("It looks like you are trying to convert chemfig format to chemfig." + "\n" + "Please select options and use 'Apply' button to modify the current structure")};
    });

        
    $('#check_update').on('click', function(){
	if ($("#txt_area").val().indexOf("%") == -1)
	    {
		alert("First, you need to convert SMILES or MOL format to chemfig and then use 'Apply' button")
	    }
	else 
	    {
	function get_check_value() {
	    var p=[];		
	    $('input[name="check"]:checked').each(function () {
		p.push(this.value);
	    });	
	    return p.join(',');
	}
	smiles_mol = last_content;
	angle = $('input[name="angle"]').val();
	hydrogens = $('#H2 :selected').text();		
	$.ajax ({
	    type: "GET",
	    url: "/mol_2_chemfig/update",
	    data: {"smiles_mol": smiles_mol, "check": get_check_value(), "angle": angle, 'hydrogens': hydrogens},			    
	    success: function(data4){				
		$("#txt_area").val(data4.chem_fig);
		$("#pdf").attr('src', data4.pdf_link);
	    },
	    error: function(Error) {
		console.log(error)
	    }
	})
	}
    });
    $('#check_reset').on('click', function(){
        $('input[name="check"]').attr('checked', false);
        $('input[name="angle"]').val('0.0');
        $('#H2').val('keep');
    });
    
    $("#txt_area").keyup(function(e){
	
	// Making sure it applies to chemfig format only, not to smiles or mol format.
	if ($("#txt_area").val().indexOf("%") != -1)
	    {
		// Ignoring Shift and arrows key in live update
		var code = (e.keyCode || e.which);
		if(code == 16 || code == 32 || code == 37 || code == 38 || code == 39 || code == 40 ) {
		    return;
		}
		smiles_mol = $("#txt_area").val();
		$.ajax ({
		    type: "GET",
		    url: "/mol_2_chemfig/update_chemfig",
		    data: {"smiles_mol": smiles_mol},		    
		    success: function(data5){
			if (data5.pdf_link == 'pdf generation foobared')
			  {
			     $("#pdf").attr('src', "static/files/broken.pdf"); 
			  }
		      else{ $("#pdf").attr('src', data5.pdf_link);}
			
		    },
		    error: function(Error) {
			console.log(error)
		    }
		})
	   }

    });
});



