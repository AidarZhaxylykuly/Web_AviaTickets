import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router, RouterModule, Routes} from '@angular/router';
import {TourService} from "../tour.service";
import {Location, NgIf} from "@angular/common";

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterModule, NgIf],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent implements OnInit{
  logged: boolean = false;

  constructor(private location: Location){
  }

  ngOnInit(): void {
    const access = localStorage.getItem("access");
    if (access) {
      this.logged = true;
    }
  }

  logout() {
    this.logged = false;
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    this.location.back();
  }
}
