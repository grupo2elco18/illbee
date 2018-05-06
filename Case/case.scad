pcb_width = 32;
pcb_thickness = 2;
pcb_length = 109;

pcb_margin = 1;

ec_width_top = 26.5;
ec_height_top = 14;
ec_length_top = 94;
ec_width_botton = 18;
ec_height_botton = 12.5;
ec_length_botton = 60;

cam_pcb_width = 15.5;
cam_pcb_length = 30;
cam_pcb_onset = 10;
cam_support_length = 10;

cam_width = 9;
cam_heigth = 10;
cam_length = 5.5;
cam_offset = 24;
cam_hole_dia = 10;

chr_pcb_width = 17;
chr_pcb_length = 42; //27;
chr_hole_offset = 1;
chr_hole_height = 4;
chr_hole_width = 8.5;
chr_hole_length = 9;
chr_hole_out = 1;

ec_z_offset = -5;

wall_thickness = 2;

back_support_len = 10;

screw_dia = 4;
screw_head_dia = 7;

/*****************************************************************************/

part = 1;
/*
FULL = 0
TOP = 1
BOTTON = 2
 */
/******************************************************************************/

ext_dia = pcb_width + wall_thickness*2;
case_length =
	pcb_length
	+ chr_pcb_length
	+ cam_pcb_length
	+ wall_thickness*2
	- cam_pcb_onset;
echo(str("Total length = ", case_length));

cone_pos = chr_pcb_length + ec_length_top + wall_thickness + pcb_margin;

pcb_support = (pcb_width - ec_width_top)/2- pcb_margin;

max_dia = ext_dia/cos(360/12);

/******************************************************************************/



if(part == 0){

	%translate([wall_thickness, 0, 0]) {
		electronics();
	}

	case(case_length, cone_pos);

	translate([chr_pcb_length, 0, 0]) {
		support_pcb(pcb_length*0.7);
	}

	support_cam();

	back_cover();

	back_support(back_support_len);

}else if(part == 1){

	translate([0, 0, ext_dia/2]) rotate([180, 0, 0]) {
		%translate([wall_thickness, 0, 0]) {
			electronics();
		}

		intersection() {
			case(case_length, cone_pos);

			translate([-1, -max_dia/2-1, 0]){
				cube(size=[case_length+2, max_dia+2, max_dia]);
			}
		}

		intersection(){
			union() {
				translate([chr_pcb_length, 0, 0]) {
					support_pcb(pcb_length*0.7);
				}

				back_support(back_support_len);
			}

			union() {
				translate([-1, -max_dia/2-1, 0]){
					cube(size=[case_length+2, max_dia+2, max_dia]);
				}

				translate([-1, -pcb_width/2, pcb_thickness+ec_z_offset-0.1]){
					cube(size=[case_length+2, pcb_width, max_dia]);
				}
			}

		}
	}






}else if(part == 2){

	translate([0, 0, ext_dia/2]) {

		%translate([wall_thickness, 0, 0]) {
			electronics();
		}

		difference() {
			union() {
				case(case_length, cone_pos);

				difference() {
					union() {
						translate([chr_pcb_length, 0, 0]) {
							support_pcb(pcb_length*0.7);
						}

						back_support(back_support_len);
					}


					translate([-1, -pcb_width/2, pcb_thickness+ec_z_offset-0.1]){
						cube(size=[case_length+2, pcb_width, max_dia]);
					}
				}
			}
			translate([-1, -max_dia/2-1, 0]){
				cube(size=[case_length+2, max_dia+2, max_dia]);
			}
		}

		back_cover();
		support_cam();
	}

}



/******************************************************************************/

module back_support(length){
	intersection() {
		translate([length/2+wall_thickness, 0]) difference() {
			cube(size=[length, max_dia, max_dia], center=true);
			cube(size=[length+1, pcb_width-2*pcb_support, max_dia+1], center=true);
		}
		rotate([0, 90, 0]) rotate([0, 0, 360/12]) {
			hexagon(ext_dia, length);
		}
	}
}

module back_cover() {
	difference() {
		rotate([0, 90, 0]) rotate([0, 0, 360/12]) {
			hexagon(ext_dia, wall_thickness, t=wall_thickness);
		}

		translate([-1, -chr_hole_width/2, pcb_thickness]) {
			cube(size=[wall_thickness+2, chr_hole_width, chr_hole_height]);
		}
	}
}

module support_cam() {
	intersection() {
		translate([chr_pcb_length+pcb_length+wall_thickness+cam_support_length/2, 0, 0]){
			difference() {
				translate([1, 0, +pcb_thickness/2-ext_dia/2]) {
					cube(size=[cam_support_length, ext_dia, ext_dia], center=true);
				}

				translate([0, 0, +0.5]) {
					cube(size=[cam_pcb_length, cam_pcb_width, pcb_thickness+1], center=true);
				}

			}
		}
		translate([cone_pos, 0, 0]) rotate([0, 90, 0]) rotate([0, 0, 360/12]) {
			case_end(
				ext_dia,
				cam_hole_dia/2+wall_thickness,
				case_length-cone_pos,
				t = wall_thickness-0.1
			);
		}
	}
}

module support_pcb(length) {

	translate([length/2 + wall_thickness, 0, 0]) {
		intersection() {
			difference() {
				cube(size=[length, max_dia+1, max_dia+1], center=true);
				translate([0, 0, ec_z_offset+pcb_thickness/2]) {
					cube(size=[length+1, pcb_width, pcb_thickness], center=true);
				}
				cube(size=[length+1, pcb_width - pcb_support*2, ext_dia+2], center=true);
			}
			translate([-length/2, 0, 0]) {
				rotate([0, 90, 0]) rotate([0, 0, 360/12]) {
					hexagon(ext_dia, length);
				}
			}
		}
	}
}

module case(length, cone){
	rotate([0, 90, 0]) rotate([0, 0, 360/12]) {
		hexagon_hollow(ext_dia, cone, wall_thickness);
		translate([0, 0, cone]){
			difference() {
				case_end(
					ext_dia,
					cam_hole_dia/2+wall_thickness,
					length-cone
				);
				case_end(
					ext_dia,
					cam_hole_dia/2+wall_thickness,
					length-cone,
					t = wall_thickness
				);
			}
		}
	}
}

module case_end(r1, r2, length, t=0){
	$fn = 50;
	translate([0, 0, -1]) intersection() {
		hexagon(r1, length + 1, t=t);
		translate([0, 0, 1]) cylinder(
			r1=r1/cos(366/12)/2 - t,
			r2=r2 - t,
			h=length);
	}
	if(t>0){
		translate([0, 0, length]) cylinder(r=r2 - t, h=2, center=true);
		translate([0, 0, -1]) hexagon(r1, 2, t=t);
	}
}


module hexagon_hollow(ext_dia, h, thickness) {
	difference() {
		hexagon(ext_dia, h);
		translate([0, 0, -1]) hexagon(ext_dia, h+2, t=thickness);
	}
}

module hexagon(ext_dia, h, t=0) {
	cylinder(d=ext_dia/cos(366/12)-t*2, h=h, $fn = 6);
}



module electronics() {
	translate([chr_pcb_length, 0, ec_z_offset]) {
		color("green"){
			translate([0, -pcb_width/2, 0]){
				cube(size=[pcb_length, pcb_width, pcb_thickness]);
			}
			translate([
				pcb_length - cam_pcb_onset,
				-cam_pcb_width/2,
				-pcb_thickness/2-ec_z_offset
			]) {
				cube(size=[cam_pcb_length, cam_pcb_width, pcb_thickness]);
			}
			translate([-chr_pcb_length, -chr_pcb_width/2, -ec_z_offset]) {
				cube(size=[chr_pcb_length, chr_pcb_width, pcb_thickness]);
			}
		}
		color("SteelBlue"){
			translate([0, -ec_width_top/2, 0]){
				cube(size=[ec_length_top, ec_width_top, ec_height_top]);
			}
			translate([0, -ec_width_botton/2, -ec_height_botton+pcb_thickness]){
				cube(size=[ec_length_botton, ec_width_botton, ec_height_botton]);
			}
		}

		color("black"){
			translate([
				pcb_length + cam_offset + cam_length/2 - cam_pcb_onset,
				0,
				-ec_z_offset
			]) {
				cube(size=[cam_length, cam_width, cam_heigth], center=true);
			}
		}

		color("Silver"){
			translate([
				-chr_pcb_length - chr_hole_out,
				-chr_hole_width/2,
				pcb_thickness - ec_z_offset
			]) {
				cube(size=[chr_hole_length, chr_hole_width, chr_hole_height]);
			}
		}
	}

}
