import { Component, OnInit } from '@angular/core';
import {AviaTour, Hotel, Reservation, UnitUser} from "../models";
import { ViewChild } from '@angular/core';
import {ActivatedRoute, Router, RouterLink} from '@angular/router';
import {TourService} from "../tour.service";
import {CommonModule, NgForOf, NgIf} from "@angular/common";
import {FormsModule} from "@angular/forms";
import {HeaderComponent} from "../header/header.component";
import {FooterComponent} from "../footer/footer.component";

@Component({
  selector: 'app-tour-detail',
  standalone: true,
  imports: [FormsModule, CommonModule, RouterLink, NgForOf, NgIf, HeaderComponent, FooterComponent],
  templateUrl: './tour-detail.component.html',
  styleUrl: './tour-detail.component.css'
})
export class TourDetailComponent implements OnInit{
  logged: boolean = false;
  tour!: AviaTour;
  hotels!: Hotel[];
  reservation: Reservation = {
    acceptance: false,
    aviatour: 0,
    hotel: 0,
    num_of_people: 0,
    total_cost: 0,
    unit_user: 1,
    user_id: 0
  };


  constructor(private tourService: TourService, private route: ActivatedRoute){

  }

  ngOnInit(): void {
    this.getTour();
    this.getHotels();
    this.updateTotalCost()

    const access = localStorage.getItem("access");
    if (access) {
      this.logged = true;
    }
  }

  getTour(){
    this.route.paramMap.subscribe((params) => {
      const tourId: number = Number(params.get('id'))
      this.tourService.getTour(tourId).subscribe((tour) => {
        this.tour = tour;
        this.reservation.aviatour = tourId;
      })
    })
  }

  getHotels(){
    this.tourService.getHotels().subscribe((hotels) => {
      this.hotels = hotels;
    })
  }

  addReservation(){
    if(this.reservation.hotel!==0 &&
    this.reservation.num_of_people>0 &&
      this.reservation.acceptance){
      this.reservation.hotel = +this.reservation.hotel;
      this.updateTotalCost();
      this.tourService
        .createReservation(this.reservation)
        .subscribe((data) => {
        })
    }else{
      alert("Please, fill out all rows")
    }
  }

  updateTotalCost(): void {
    const selectedHotel = this.hotels.find(hotel => hotel.id === this.reservation.hotel);
    if (selectedHotel) {
      const costPerPerson = selectedHotel.cost_per_person;
      this.reservation.total_cost = this.reservation.num_of_people * (costPerPerson + this.tour.cost);
    }
  }
}
