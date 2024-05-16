package org.acvy.gsteam.entities;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;


@Getter @Setter
@AllArgsConstructor @NoArgsConstructor
@Entity @Table(name = "service_user")
public class ServiceUser {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    private String password;
    private String email;

    ServiceUser(ServiceUser other)
    {
        this.id = other.id;
        this.username = other.username;
        this.password = other.password;
        this.email = other.email;
    }
}
