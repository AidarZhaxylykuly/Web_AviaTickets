import {Component, ElementRef, OnInit} from '@angular/core';
import {AviaTour, Reservation} from "../models";
import {TourService} from "../tour.service";
import {ActivatedRoute} from "@angular/router";
import {NgForOf} from "@angular/common";
import {HeaderComponent} from "../header/header.component";
import {FooterComponent} from "../footer/footer.component";

@Component({
  selector: 'app-my-reservations',
  standalone: true,
  imports: [
    NgForOf,
    HeaderComponent,
    FooterComponent
  ],
  templateUrl: './my-reservations.component.html',
  styleUrl: './my-reservations.component.css'
})
export class MyReservationsComponent implements OnInit{
  reservations: Reservation[] = [];
  loaded = false;

  constructor(private tourService: TourService, private route: ActivatedRoute, private elementRef: ElementRef) { }

  ngOnInit(): void {
    this.getReservations();
  }

  getReservations() {
    this.tourService.getReservations().subscribe((reservations: Reservation[]) => {
      this.reservations = reservations;
      this.loaded = true;
      this.loadAviaToursInfo();
    });
  }

  loadAviaToursInfo() {
    this.reservations.forEach(reservation => {
      this.tourService.getTour(reservation.aviatour).subscribe((aviaTour: AviaTour) => {
        reservation.aviaTourDetails = aviaTour;
      });
    });
  }
}
