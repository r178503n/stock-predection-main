import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SweetAlertService } from 'src/app/application-shared/services/sweetAlert/sweetAlert.service';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss'],
})
export class NavigationComponent implements OnInit {
  visibleSidebar1;
  constructor(
    private sweetAlert: SweetAlertService,
    //  private authService: RestAuthService,
    // public generalService: GeneralService,
    private router: Router
  ) {}

  ngOnInit(): any {}
 
}
