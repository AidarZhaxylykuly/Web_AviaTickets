import {Component, ElementRef, OnInit} from '@angular/core';
import {AviaTour} from "../models";
import { ViewChild } from '@angular/core';
import {ActivatedRoute, Router, RouterLink} from '@angular/router';
import {TourService} from "../tour.service";
import {CommonModule, NgForOf, NgIf} from "@angular/common";
import {HeaderComponent} from "../header/header.component";


@Component({
  selector: 'app-tour-list',
  standalone: true,
  imports: [
    RouterLink,
    NgForOf,
    NgIf,
    CommonModule,
    HeaderComponent
  ],
  templateUrl: './tour-list.component.html',
  styleUrl: './tour-list.component.css'
})


export class TourListComponent implements OnInit{
  tours!: AviaTour[];
  loaded = false;


  constructor(private tourService: TourService, private route: ActivatedRoute, private elementRef: ElementRef){

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

  scrollToElement(): void {
    const targetElement = this.elementRef.nativeElement.querySelector('#sec');
    if (targetElement) {
      targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
}
