import {RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { SigninComponent } from './signin/signin.component';
import { AviamainComponent } from './aviamain/aviamain.component';
import { SignupComponent } from './signup/signup.component';
import {TourListComponent} from "./tour-list/tour-list.component";
import {TourDetailComponent} from "./tour-detail/tour-detail.component";


export const routes: Routes = [
    {path: '', component: AviamainComponent},
    {path: 'tours', component: TourListComponent, title: 'Avia Tours'},
    {path: 'signin', component: SigninComponent},
    {path: 'signup', component: SignupComponent},
    {path: 'tours/:id', component: TourDetailComponent},
];

