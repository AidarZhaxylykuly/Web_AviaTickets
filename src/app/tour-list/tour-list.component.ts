import { Component, OnInit } from '@angular/core';
import {AviaTour} from "../models";
import { ViewChild } from '@angular/core';
import {ActivatedRoute, Router, RouterLink} from '@angular/router';
import {TourService} from "../tour.service";
import {CommonModule, NgForOf, NgIf} from "@angular/common";


@Component({
  selector: 'app-tour-list',
  standalone: true,
  imports: [
    RouterLink,
    NgForOf,
    NgIf,
    CommonModule
  ],
  templateUrl: './tour-list.component.html',
  styleUrl: './tour-list.component.css'
})


export class TourListComponent implements OnInit{
  tours!: AviaTour[];
  loaded = false;


  constructor(private tourService: TourService, private route: ActivatedRoute){

  }

  ngOnInit(): void {
    this.getTours();
  }

  getTours(){
    this.tourService.getTours().subscribe((tours) => {
      this.tours = tours;
      this.loaded = true;
    })
  }
}
