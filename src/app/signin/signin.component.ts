import {Component, OnInit} from '@angular/core';
import { FooterComponent } from '../footer/footer.component';
import {ActivatedRoute, Router, RouterModule} from '@angular/router';
import {TourService} from "../tour.service";
import {FormsModule} from "@angular/forms";


@Component({
  selector: 'app-signin',
  standalone: true,
  imports: [FooterComponent, RouterModule, FormsModule],
  templateUrl: './signin.component.html',
  styleUrl: './signin.component.css'
})
export class SigninComponent implements OnInit{
  username: string = '';
  password: string = '';
  logged: boolean = false;

  constructor(private tourService: TourService, private route: ActivatedRoute, private router: Router){

  }

  ngOnInit(): void {
    const access = localStorage.getItem("access");
    if (access) {
      this.logged = true;
    }
  }

  login(){
    this.tourService.
    login(this.username, this.password).
    subscribe((data)=>{
      this.logged = true;
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      this.router.navigate(['']);
    })
  }

  logout() {
    this.logged = false;
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
  }
}
