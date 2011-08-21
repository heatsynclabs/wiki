<div style="float: right">

</div>

Return to [UAS](UAS)

## Avionics

### Controller

Embedded controller: Arduino or clone.

The following as interesting and already in inventory: Arduino Decemilia, Arduino Uno, Arduino Mega 2560, [Maple Mini](http://leaflabs.com/devices/#Maple-Mini), Maple (Rev5).

### Sensors

- This is the initial sensor package:
  - [LS20031 GPS](http://www.pololu.com/catalog/product/1249)
  - [Accelerometer](http://www.pololu.com/catalog/product/1250) (3 axis) also includes magnetometer
  - [Barometric Pressure/Temperature Sensor](http://www.pololu.com/catalog/product/1617) (We might need greater accuracy.)
  - [L3G4200D Gyro](http://www.pololu.com/catalog/product/1272) (3 axis) also has a temp sensor
  - [Proximity Sensor](http://www.pololu.com/catalog/product/723)

|  |  |  |  |
|----|----|----|----|
| Sensor Type | Nominal Power | Voltage Req | Temp Ranges (C) |
| GPS Module (LS20031) | 29.000 mA | 3.0 - 4.2 V |  |
| Compass & Accelerometer (LSM303DLH) | 00.830 mA | 2.5 - 3.3 V |  |
| Barometer (MPL115A1) | 00.010 mA | 2.4 - 5.5 V |  |
| 3-Axis Gyro (L3G4200D) | 06.100 mA | 2.4 - 3.6 V | -40 to +85 |
| Sonar Range Finder (MB1000) | 02.000 mA | 2.5 - 5.5 V |  |
| **Total** | **37.940 mA** | **3.0 - 3.3 V** |  |

- still looking for a good altimeter, a replacement for DTED lookup

## Aircraft

### Airframe

The initial airframe must forgive mediocre piloting. We want docile flight characteristics combined with a rugged air frame.

Try to select a craft with spares to reduce cost of reconstruction.

These are our top candidates:

- [Radian Pro](http://www.parkzone.com/Products/Default.aspx?ProdID=PKZ5475) -- ([YouTube](http://www.youtube.com/watch?v=tDVpYsK9kww&feature=player_embedded)) (Note the Radian Pro has AIL, FLAP, ELV, & RUD the Radian standard has only ELV & RUD only)
- [Phoenix Glider](http://www.hobbyking.com/hobbyking/store/__13994__Phoenix_2000_EPO_Composite_R_C_Glider_Plug_Fly_.html) Pretty cool name... If the avionics fit into the cockpit I say go for it. (Note that we can add flaps!)
  - Alternate [source](http://store.economyrc.com/phoenix2000-rtf-arf-kit-glider-rcairplane.html)
- [Bixler](http://www.hobbyking.com/hobbyking/store/__18083__Hobbyking_Bixler_EPO_1400mm_ARF_USA_Warehouse_.html) Looks like a good place to start. Lots of surfaces to control, plenty of room for avionics, and reasonably priced.
- Multiplex Cularis (2.6m) available as [kit](http://multiplexusa.com/model-kits/cularis.html) or [RR](http://multiplexusa.com/rr-rtf-models/receiver-ready/cularis-rr.html) (Note the Easy Glider Pro, also...)

These are interesting alternatives:

- [HobbyKing SkyFun](http://www.hobbyking.com/hobbyking/store/uh_viewItem.asp?idProduct=9614) Flying wing. Minimal surfaces.
- [Predator](http://www.hobbyking.com/hobbyking/store/__5455__Predator_UAV_74in_Spy_Plane_ARF.html) Fairly large. Lots of goodness?
  - [review](http://www.hobbyking.com/hobbyking/forum/forum_posts.asp?TID=719) great info.
- [Reaper](http://www.hobbyking.com/hobbyking/store/__17988__MQ_9_Reaper_Fiberglass_2500mm_FPV_ARF_.html) cool.
- [Van's RV-9](http://www.e-fliterc.com/Products/Default.aspx?ProdID=EFL2775) too cool, experimental!
- [3m wingspan](http://sd-model.en.alibaba.com/product/290063229-200395223/rc_airplane_3000mm_fiberglass_glider.html) big and light
- [4m wing span](http://hobbyfly.com/en/airplane-47/sailplanes-137/discus-cs-4000mm-glider-arf-2172.html) huge, does not look like 12 ft

### Surface Control

- [Servos](http://www.hobbypartz.com/standardservos.html) X 4
  - want light ones, but strong enough to control the surfaces, might need to get the craft before we order/change the servos

## Comms

- XBee PRO 900 XSC? or...?

## Miscellaneous

- [Camera?](http://www.hobbyking.com/hobbyking/store/uh_viewItem.asp?idProduct=13987)
