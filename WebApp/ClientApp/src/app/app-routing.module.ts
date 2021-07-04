import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PageNotFoundComponent } from './application-shared/components/page-not-found/page-not-found.component';
import { NavigationComponent } from './modules/navigation/components/navigation/navigation.component';

const routes: Routes = [
 
  {
    path: '',
    component: NavigationComponent,
    loadChildren: () =>
      import('./modules/navigation/navigation.module').then(
        (mod) => mod.NavigationModule
      ),
  },

  
  // 404 page
  { path: '**', component: PageNotFoundComponent },


  { path: '**', redirectTo: '', pathMatch: 'full' },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
